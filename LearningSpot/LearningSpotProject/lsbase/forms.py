from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# custom user creation form building on the django standard
class CreateUser(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']