from django.shortcuts import redirect, render, get_object_or_404
from .models import Learning_Intention, Happy_Select, Sad_Select, Unsure_Select

def index(request):
    return render(request, 'index.html')

def student(request):
    learning_intentions = learning_intention.objects.all()
    learning_tasks = learning_task.objects.all()
    user = request.user

    dynamic_content = {'learning_intentions' : learning_intentions, 'learning_tasks' : learning_tasks, 'user' : user}
    
    return render(request, 'student.html', dynamic_content)


def teacher(request):
    learning_intentions = learning_intention.objects.all().order_by('created')
    learning_tasks = learning_task.objects.all().order_by('created')

    dynamic_content = {'learning_intentions' : learning_intentions, 'learning_tasks' : learning_tasks}
    return render(request, 'teacher.html', dynamic_content)



def li(request):
    learning_intentions = learning_intention.objects.all()
    user = request.user

    dynamic_content = {'learning_intentions' : learning_intentions, 'user' : user}
    
    return render(request, 'li.html', dynamic_content)


#------------------------------------------------------

def learning_intention(request):
    qs = Learning_Intention.objects.all()
    user = request.user

    context = {
        'qs':qs,
        'user':user,
    }

    return render (request,'main.html', context)


def happy_select(request):
    user = request.user
    if request.method == 'POST':
        learning_intention_id = request.POST.get('learning_intention_id')
        learning_intention_obj = Learning_Intention.objects.get(id=learning_intention_id)

        if user in learning_intention_obj.happy.all():
            learning_intention_obj.happy.remove(user)
        else:
            learning_intention_obj.happy.add(user)

        
        happy, created = Happy_Select.objects.get_or_create(user=user, learning_intention_id=learning_intention_id)

        if not created:
            if happy.value == 'Select':
                happy.value = 'Unselect'
            else: 
                happy.value = 'Select'
        
        happy.save()

    return redirect('learning_intention')



def unsure_select(request):
    user = request.user
    if request.method == 'POST':
        learning_intention_id = request.POST.get('learning_intention_id')
        learning_intention_obj = Learning_Intention.objects.get(id=learning_intention_id)

        if user in learning_intention_obj.unsure.all():
            learning_intention_obj.unsure.remove(user)
        else:
            learning_intention_obj.unsure.add(user)

        
        unsure, created = Unsure_Select.objects.get_or_create(user=user, learning_intention_id=learning_intention_id)

        if not created:
            if unsure.value == 'Select':
                unsure.value = 'Unselect'
            else: 
                unsure.value = 'Select'
        
        unsure.save()

    return redirect('learning_intention')



def sad_select(request):
    user = request.user
    if request.method == 'POST':
        learning_intention_id = request.POST.get('learning_intention_id')
        learning_intention_obj = Learning_Intention.objects.get(id=learning_intention_id)

        if user in learning_intention_obj.sad.all():
            learning_intention_obj.sad.remove(user)
        else:
            learning_intention_obj.sad.add(user)

        
        sad, created = Sad_Select.objects.get_or_create(user=user, learning_intention_id=learning_intention_id)

        if not created:
            if sad.value == 'Select':
                sad.value = 'Unselect'
            else: 
                sad.value = 'Select'
        
        sad.save()

    return redirect('learning_intention')