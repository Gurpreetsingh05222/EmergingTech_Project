from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, ContactForm, UpdateForm
from .models import Post, User, Comment, ContactUs, Like
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class GetUserDetails(generic.DetailView):
    queryset = Post.objects.all()
    template_name = 'post_detail_profile.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        # profile = User.objects.all()
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()
        return redirect('/')


class UpdatePostView(generic.UpdateView):
    form_class = UpdateForm
    model = Post
    template_name = 'update_post.html'
    success_url = "/"

class GetAllPosts(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

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
        next = request.POST.get('next', '')
        post = request.POST.get('post', '')
        print(next)
        print(post)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        context = {'login_error' : None, 'register_error': None, 'register_success': None}
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next is not None and next != '':
                return redirect(next, {'post' : post })

            return redirect('/', {'post_list': Post.objects.order_by('-created_on')})
        else:
            template = loader.get_template('sign_in.html')
            if email!="":
                request_form = request.POST
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    new_user = User.objects.create_user(request_form['username'], request_form['email'], request_form['password1'])
                    new_user.first_name = request_form['first_name']
                    new_user.last_name = request_form['last_name']
                    new_user.save()
                    user = authenticate(request, username=new_user.username, password=request_form['password1'])
                    print(user)
                    if user is not None:
                        context = {'register_success': 'Registered successfully! Log in now!'}
                        if next is not None and next != '':
                            login(request, user)
                            return redirect(next, {'post' : post })
                    else:
                        context = {'register_error': 'Invalid details! Unable to sign up!'}
                else:
                    context = {'register_error': 'Invalid details! Unable to sign up!'}
            else:
                context = {'login_error': 'Username or Password is invalid!'}

            context["next"] = next
            context["post"] = post
            print(context)
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