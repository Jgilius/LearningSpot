from django.shortcuts import render
from .models import learning_intention
from .models import learning_task

def index(request):
    return render(request, 'index.html')

def home(request):
    learning_intentions = learning_intention.objects.all().order_by('created')
    return render(request, 'home.html', {'learning_intentions' : learning_intentions},)

    
# {'learning_tasks' : learning_tasks}
#   learning_tasks = learning_task.objects.all().order_by('created')