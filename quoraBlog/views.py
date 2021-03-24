from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from .forms import TextInput

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

@login_required
def profile(request):
    return render(request, 'profile.html')

def blogs(request):
    return render(request, 'blogs.html')

def txt_sum(req):
    summary=''
    #fulltext = request.POST.get('text_inp','')
    if(req.method == 'POST'):
        form = TextInput(req.POST)
        if (form.is_valid()):
            n = form.cleaned_data.get('input1')
            
            r = requests.post(
                "https://api.deepai.org/api/summarization",
                data={
                    'text': n,
                },
                headers={'api-key': 'd45f7c67-f01d-44e9-9615-335b2d3ba0b9'}
                )
            a=r.json()
            summary=a['output']
    else:
        form = TextInput()
    return render(req, 'txt_sum.html',{'form': form, 'summary':summary})

class PostCreateView(CreateView):
    model= Post
    fields =['title', 'content',]
    success_url ='/blogs'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

