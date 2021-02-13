from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, 'homePage.html', {})
    
def about(req):
    return render(req, 'about.html', {})