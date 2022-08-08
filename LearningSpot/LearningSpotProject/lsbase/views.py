from django.shortcuts import render
from .models import learning_intention
from .models import learning_task

def index(request):
    return render(request, 'index.html')

def home(request):
    learning_intentions = learning_intention.objects.all().order_by('created')
    learning_tasks = learning_task.objects.all().order_by('created')

    dynamic_content = {'learning_intentions' : learning_intentions, 'learning_tasks' : learning_tasks}
    return render(request, 'home.html', dynamic_content)

    
# {'learning_tasks' : learning_tasks}
#   learning_tasks = learning_task.objects.all().order_by('created')