from django.shortcuts import render
from .models import learning_intention

def index(request):
    return render(request, 'index.html')

def home(request):
    learning_intentions = learning_intention.objects.all().order_by('created')
    return render(request, 'home.html', {'learning_intentions' : learning_intentions})