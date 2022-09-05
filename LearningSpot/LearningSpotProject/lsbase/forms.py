from tokenize import group
from turtle import title
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Learning_Intention, Learning_Task
from django.forms import ModelForm

# custom user creation form building on the django standard
class CreateUser(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateLI(ModelForm):
    class Meta:
        model = Learning_Intention
        fields = ['title']


class CreateLT(ModelForm):
    class Meta:
        model = Learning_Task
        fields = ['title']