from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('home/', views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('test/', views.login, name='login'),
    path('txt_sum/', views.txt_sum, name='txt_sum'),
    path('blogs/', views.blogs, name='blogs'),
]