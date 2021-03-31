from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisteration

def register(req):
    if(req.method == 'POST'):
        form = UserRegisteration(req.POST)
        if (form.is_valid() and str(form.cleaned_data.get('email')).find('somaiya.edu') != -1):
            form.save()
            print(form.cleaned_data.get('email'))
            print(str(form.cleaned_data.get('email')).find('somaiya.edu'))
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisteration()
    return render(req, 'register.html', {'form': form})