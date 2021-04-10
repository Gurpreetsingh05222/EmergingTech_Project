from django.urls import path
from . import views



urlpatterns = [
    path('', views.GetAllPosts.as_view(), name='home'),
    path('<slug:slug>/', views.GetPostDetails.as_view(), name='post_detail'),
]