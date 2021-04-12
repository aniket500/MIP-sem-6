from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisteration
from django.core.mail import send_mail
from django.conf import settings

def register(req):
    if(req.method == 'POST'):
        form = UserRegisteration(req.POST)
        # print(str(form.cleaned_data.get('email')))
        if (form.is_valid() and str(form.cleaned_data.get('email')).find('somaiya.edu') != -1):
            print('form is VALID !!')
            form.save()
            print(form.cleaned_data.get('email'))
            print(str(form.cleaned_data.get('email')).find('somaiya.edu'))
            send_mail(
                'Verify your account',
                'Open this link to verify your account',
                settings.EMAIL_HOST_USER,
                [str(form.cleaned_data.get('email'))],
                # fail_silently=False,
            )
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisteration()
    return render(req, 'register.html', {'form': form})