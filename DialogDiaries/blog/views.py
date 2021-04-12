from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Post, User
from django.contrib.auth import authenticate, login, logout


class GetAllPosts(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

class GetPostDetails(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class GetSignIn(generic.TemplateView):
    model = User
    template_name = 'sign_in.html'

@csrf_exempt
class GetUserView(generic.TemplateView):
    def LogInUser(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/', {'post_list': Post.objects.order_by('-created_on')})
        else:
            return redirect('/sign-in/')

    def LogOut(request):
        logout(request)
        return redirect('/')

