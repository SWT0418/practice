from django import forms
from django.forms import fields
from .models import Blog,Comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'hashtags', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']