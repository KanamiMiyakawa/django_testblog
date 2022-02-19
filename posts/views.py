from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("Hello World!")
    posts = Post.objects.order_by('-pulished')
    return render(request, 'posts/index.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})
# Create your views here.
