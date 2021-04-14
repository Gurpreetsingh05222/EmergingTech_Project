from django.urls import path
from . import views



urlpatterns = [
    path('', views.GetAllPosts.as_view(), name='home'),
    path('create/', views.CreatePostView.as_view(), name='post_new'),
    path('sign-in/', views.GetSignIn.as_view(), name='sign_in'),
    path('sign-out/', views.GetUserView.LogOut, name='sign_out'),
    path('sign-in/authenticate/', views.GetUserView.LogInUser, name='authenticate'),
    #path('sign-in/authenticate/', views.GetUserView.LogInUser, name='sign_in'),
    path('<slug:slug>/', views.GetPostDetails.as_view(), name='post_detail'),
]