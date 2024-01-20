from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from .forms import CommentForm, PostForm

from blog.models import Post, Comment


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk,):
    posts = Post.objects.all().order_by("-created_on")
    # Récupération de l'objet Post (article de blog) associé à la clé primaire (pk)
    post = get_object_or_404(Post, pk=pk)
    # Initialisation du formulaire de commentaire en dehors de la condition
    form = CommentForm()

    # Vérification si la requête HTTP est de type POST (soumission de formulaire)
    if request.method == "POST":
        # Création d'une instance de CommentForm avec les données POST
        form = CommentForm(request.POST)

        # Vérification si le formulaire de commentaire est valide
        if form.is_valid():
            # Création d'un nouvel objet Comment avec les données du formulaire
            parent_comment_id = form.cleaned_data.get("parent_comment")
            parent_comment = None

            if parent_comment_id:
                # S'il y a un commentaire parent, récupérez-le
                parent_comment = Comment.objects.get(id=parent_comment_id)

            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
                parent_comment=parent_comment,  # Associez le commentaire parent le cas échéant
            )
            # Enregistrement du commentaire dans la base de données
            comment.save()

    # Récupération de tous les commentaires associés à l'article de blog
    comments = Comment.objects.filter(post=post).order_by("created_on")

    # Création du contexte avec l'objet post, les commentaires et le formulaire
    context1 = dict(post=post, comments=comments, form=form)
    context2 = {"posts": posts}
    merged_context = {**context1, **context2}

    # Rendu du modèle "blog_detail.html" avec le contexte spécifié
    return render(request, "try.html", merged_context)


def blog_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("blog-index")


def blog_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog-index", pk=post.pk)
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "blog_create.html", context)


def blog_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                post=post, author=request.user, body=form.cleaned_data["body"]
            )
            comment.save()
            comment.post = post
            comment.author = str(request.user)
            comment.save()
            return redirect("blog-detail", pk=post.pk)

    else:
        form = CommentForm()

    return render(request, "blog_add_comment.html", {"form": form})


def comment_comment(request, comment_id, post_id):
    # Récupération de l'objet Post associé au post_id
    post = get_object_or_404(Post, pk=post_id)

    # Récupération de l'objet Comment associé au comment_id
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        # Création d'une instance du formulaire de commentaire avec les données POST
        form = CommentForm(request.POST)
        if form.is_valid():
            # Création d'un nouveau commentaire lié au commentaire parent
            new_comment = Comment(
                parent_comment=comment,
                author=str(request.user),
                body=form.cleaned_data["body"],
                post=comment.post,
            )

            new_comment.save()
            return redirect("blog-detail", pk=post.pk)

        else:
            form = CommentForm()

        return render(request, "blog_comment_comment.html", {"form": form})
