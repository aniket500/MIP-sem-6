from django.shortcuts import render, redirect, reverse
from .models import Post
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from .forms import TextInput
from users.forms import UserRegisteration, UserUpdateForm, ProfileUpdateForm


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
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile was updated successfully!')
            return HttpResponseRedirect(reverse('profile'))
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html',context)

def blogs(request):
    context = {
        'allPosts': Post.objects.all()
    }
    return render(request, 'blogs.html', context)

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
            print(summary)
    else:
        form = TextInput()
    return render(req, 'txt_sum.html',{'form': form, 'summary':summary})

class PostCreateView(CreateView):
    model= Post
    fields =['title', 'content','group']
    success_url ='/blogs'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

