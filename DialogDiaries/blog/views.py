from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, ContactForm
from .models import Post, User, Comment, ContactUs, Like
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class ContactView(generic.CreateView):
    form_class = ContactForm
    model = ContactUs
    template_name = 'contact_us.html'
    success_url = '/'

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    login_url = '/sign-in'
    redirect_field_name = 'index.html'
    form_class = PostForm
    model = Post
    template_name = 'post_form.html'
    success_url = '/'

class GetAllPosts(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

class GetPostDetails(generic.TemplateView):
    def PostDetails(request, slug):
        post = Post.objects.filter(slug=slug)[0]
        template = loader.get_template('post_detail.html')
        comment_count = Comment.objects.filter(post=post).count()
        like_count = Like.objects.filter(post=post).count()
        context = {'post': post, 'total_comments': comment_count, 'total_likes': like_count}
        return HttpResponse(template.render(context, request))

class UpdatePost(generic.TemplateView):
    @login_required(login_url='/sign-in')
    def AddLike(request):
        print('authenticated')

    @login_required(login_url='/sign-in')
    def AddComment(request):
        print('authenticated')

class GetSignIn(generic.TemplateView):
    model = User
    template_name = 'sign_in.html'

# class CreateBlogPost(generic.TemplateView):
#     model = Post
#     template_name = 'create_blog_post.html'

@csrf_exempt
class GetUserView(generic.TemplateView):
    def LogInUser(request):
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        context = {'login_error' : None, 'register_error': None, 'register_success': None}
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/', {'post_list': Post.objects.order_by('-created_on')})
        else:
            template = loader.get_template('sign_in.html')
            if email!="":
                print(request.POST)
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = authenticate(request, username=username, password=password)
                    print(user)
                    if user is not None:
                        context = {'register_success': 'Registered successfully! Log in now!'}
                    else:
                        context = {'register_error': 'Invalid details! Unable to sign up!'}
                else:
                    context = {'register_error': 'Invalid details! Unable to sign up!'}
            else:
                context = {'login_error': 'Username or Password is invalid!'}
            return HttpResponse(template.render(context, request))

    def LogOut(request):
        logout(request)
        return redirect('/')


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')

def about(request):
    return render(request , 'about.html')