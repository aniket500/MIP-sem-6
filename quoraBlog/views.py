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

def home(req):
    context = {
        'keyPosts': posts,
        'title': 'Qoura',
    }
    return render(req, 'homePage.html', context)
    
def about(req):
    return render(req, 'about.html', {})