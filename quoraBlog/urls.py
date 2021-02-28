from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
<<<<<<< HEAD
    path('profile/',views.profile, name='profile')
=======
    path('register/', user_views.register, name='register'),
>>>>>>> 6d23ffa58e257baa09665367162570120477be99
]