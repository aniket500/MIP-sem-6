from django.shortcuts import render
from django.http import HttpResponse

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

def login(request):
    return render(request, 'login_ui.html')

def home(request):
    # context = {
    #     'keyPosts': posts,
    #     'title': 'Qoura',
    # }
    return render(request, 'home_ui.html')

def profile(request):
    return render(request, 'profile.html')