from django import forms
from django.db import models

from blog.models import Post


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment !"}
        )
    )
    objects = models.Manager()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
