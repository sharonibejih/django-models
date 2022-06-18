from dataclasses import fields
from django import forms
from models import Post

class PostForm(forms.Model):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "author",
            "created_date",
            "published_date"
        ]
