from django.urls import path
from . import views
from users import views as user_views
from .views import PostCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('test/', views.login, name='login'),
    path('txt_sum/', views.txt_sum, name='txt_sum'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path('blogs/', views.blogs, name='blogs'),
]