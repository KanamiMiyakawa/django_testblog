from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Post

# def index(request):
#     # return HttpResponse("Hello World!")
#     posts = Post.objects.order_by('-pulished')
#     return render(request, 'posts/index.html', {'posts': posts})

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pulished')[:5]

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})
# Create your views here.
