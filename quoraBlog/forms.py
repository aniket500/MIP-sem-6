from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TextInput(forms.Form):
    input1 = forms.CharField(label="Input", widget=forms.Textarea())

