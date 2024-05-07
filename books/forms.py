# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Comment

from django.forms.widgets import PasswordInput,TextInput
class BookSearchForm(forms.Form):
    search_query = forms.CharField(label='Search')
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    