from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Abc',
        'title': 'Post 1',
        'content': 'This is the first post',
        'date': '14 Feb, 2021',
    },
    {
        'author': 'Xyz',
        'title': 'Post 2',
        'content': 'Hey Abc are you single ?',
        'date': 'Yes',
    }
]

def login_page(request):
    return render(request, 'login_ui.html')

def login(request):
    context = {
        'keyPosts': Post.objects.all()
    }
    return render(request, 'homePage.html', context)    #login_ui.html

def home(request):
    # context = {
    #     'keyPosts': posts,
    #     'title': 'Qoura',
    # }
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def blogs(request):
    return render(request, 'blogs.html')

def txt_sum(request):
    return render(request, 'txt_sum.html')