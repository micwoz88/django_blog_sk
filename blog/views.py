from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk) # jak nie znajdzie, zwróci 404

    return render(request, 'blog/post_detail.html', {'post': post})