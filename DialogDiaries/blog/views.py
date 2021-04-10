from django.shortcuts import render
from django.views import generic
from .models import Post


class GetAllPosts(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

class GetPostDetails(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
