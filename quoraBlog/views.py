from django.shortcuts import render, redirect, reverse
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from .forms import TextInput, AddComment
from users.forms import UserRegisteration, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy


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
        'allPosts': Post.objects.all(),
        'commList': ['Computer', 'Information-Technology', 'Mechanical', 'Electronics-TeleCom', 'Electronics'],
    }
    return render(request, 'blogs.html', context)

def computers(req):
    context = {
        'community': 'Computer Engineering',
        'commPost': list(Post.objects.all()),
    }
    return render(req, 'computers.html', context)

def mech(req):
    context = {
        'community': 'Mechanical',
        'commPost': list(Post.objects.all()),
    }
    return render(req, 'computers.html', context)

def it(req):
    context = {
        'community': 'Information Technology',
        'commPost': list(Post.objects.all()),
    }
    return render(req, 'computers.html', context)

def extc(req):
    context = {
        'community': 'Electronics and Telecommunications',
        'commPost': list(Post.objects.all()),
    }
    return render(req, 'computers.html', context)

def etrx(req):
    context = {
        'community': 'Electronics',
        'commPost': list(Post.objects.all()),
    }
    return render(req, 'computers.html', context)

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model= Post
    fields =['title', 'content','group']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blogs'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AddCommentView(CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'addComment.html'
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)