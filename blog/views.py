from django.shortcuts import render, get_object_or_404
from .models import Post

def homepage(request):
    posts = Post.objects.order_by('-published_date')[:5]
    return render(request, 'blog/homepage.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
