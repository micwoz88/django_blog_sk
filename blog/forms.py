from django import forms
from .models import Post

class ImgForm(forms.ModelForm):
# class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # pola
        fields = ['title', 'text', 'image']