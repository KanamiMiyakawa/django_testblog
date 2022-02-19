from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pulished')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
# Create your views here.
