from django.urls import path
from . import views
from users import views as user_views
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, AddCommentView, LikeView, ReportView, myBlogs
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('test/', views.login, name='login'),
    path('txt_sum/', views.txt_sum, name='txt_sum'),
    path('my-blogs/', views.myBlogs, name='my-blogs'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/Computer/', views.computers, name='Computers'),
    path('blogs/Mechanical', views.mech, name='Mechanical'),
    path('blogs/Information-Technology', views.it, name='Information-Technology'),
    path('blogs/Electronics-TeleCom', views.extc, name='Electronics-TeleCom'),
    path('blogs/Electronics', views.etrx, name='Electronics'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='addComment'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('report/<int:pk>', ReportView, name='report_post'),
]