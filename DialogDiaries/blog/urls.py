from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.GetAllPosts.as_view(), name='home'),
    path('contactus/', views.ContactView.as_view(), name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('create/', views.CreatePostView.as_view(), name='post_new'),
    path('sign-in/authenticate/', views.GetUserView.LogInUser, name='authenticate'),
    re_path('sign-in', views.GetSignIn.as_view(), name='sign_in'),
    path('sign-out/', views.GetUserView.LogOut, name='sign_out'),
    path('add-likes/', views.UpdatePost.AddLike, name='add_likes'),
    path('add-comments/', views.UpdatePost.AddComment, name='add_comments'),
    #path('sign-in/authenticate/', views.GetUserView.LogInUser, name='sign_in'),
    path('<slug:slug>/', views.GetPostDetails.PostDetails, name='post_detail'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/edit/<pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('<pk>/profile/', views.UserProfileView.as_view(), name='userprofile'),
]