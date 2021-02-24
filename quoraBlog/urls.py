from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', user_views.register, name='register'),
]