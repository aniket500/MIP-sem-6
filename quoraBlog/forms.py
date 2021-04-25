from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class TextInput(forms.Form):
    input1 = forms.CharField(label="Input", widget=forms.Textarea())

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(),
            'content': forms.Textarea(),
        }