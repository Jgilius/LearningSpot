from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# -------------------------------------------------------------------------------------------------------------------------------------------------
from .decorators import user_not_authenticated, teacher_only
from .forms import CreateUser, CreateLI, CreateLT
from .models import LTComplete, LTInProgress, LTNeedHelp, LTNotStarted, Learning_Intention, Happy_Select, Learning_Task, Sad_Select, Unsure_Select



def index(request):
    return render(request, 'index.html')


# user creation view function 'registration page'
@user_not_authenticated
def register_page(request):
    form = CreateUser( )
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request, 'An account was successfully created for ' + username + '.')
            return redirect('login')
    context={'form': form}
    return render (request, 'register.html', context)
    

# user login view function 'login page'
@user_not_authenticated
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student')
        else: 
            messages.info(request, 'username OR password is incorrect, please try again.')
    context={}
    return render (request, 'login.html', context)


# user logout view function 'login page'
def user_logout(request):
    logout(request)
    return redirect('login')


# student function, contest accessing all learning intention and task objects
@login_required(login_url='login')
def student(request):
    qs = Learning_Intention.objects.all()
    lt = Learning_Task.objects.all()
    user = request.user
    context = {
        'qs':qs,
        'lt':lt,
        'user':user,
    }
    return render (request,'student.html', context)


# teacher function, contest accessing all learning intention and task objects
# contains post method a handling functionality for learning intention and task creation 
# context access for all objects associated with learning intention, task and associated forms
@login_required(login_url='login')
@teacher_only
def teacher(request):
    li = Learning_Intention.objects.all()
    lt = Learning_Task.objects.all()
    user = request.user

    formli = CreateLI()
    if request.method == 'POST' and 'li_input' in request.POST:
        formli = CreateLI(request.POST)
        if formli.is_valid():
            formli.save()

    ltform = CreateLT()
    if request.method == 'POST' and 'lt_input' in request.POST:
        ltform = CreateLT(request.POST)
        if ltform.is_valid():
            ltform.save()

    lihappy = Learning_Intention.num_happy

    context = {
        'li':li,
        'lt':lt,
        'user':user,
        'formli':formli,
        'ltform':ltform,
        'lihappy':lihappy,
    }
    return render (request,'teacher.html', context)



def learning_intention_teacher(request):
    qs = Learning_Intention.objects.all()
    context = {
        'qs':qs,
    }
    return render (request,'teacher.html', context)

def learning_intention(request):
    qs = Learning_Intention.objects.all()
    context = {
        'qs':qs,
    }
    return render (request,'student.html', context)


# select function, retreiving learning intention ID, 
# if user selecting happy is already associated to the learning intention, then upon clicking the button they are removed
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
    return redirect('student')

# select function, retreiving learning intention ID, 
# if user selecting happy is already associated to the learning intention, then upon clicking the button they are removed
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
    return redirect('student')


# select function, retreiving learning intention ID, 
# if user selecting happy is already associated to the learning intention, then upon clicking the button they are removed
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
    return redirect('student')


def learning_task(request):
    lt = Learning_Task.objects.all()
    user = request.user
    context = {
        'lt':lt,
        'user':user,
        }
    return render (request,'student', context)

# select function, retreiving learning task ID, 
# if user selecting happy is already associated to the learning task, then upon clicking the button they are removed
def inprogress_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)
        if user in learning_task_obj.inprogress.all():
            learning_task_obj.inprogress.remove(user)
        else:
            learning_task_obj.inprogress.add(user)
        inprogress, created = LTInProgress.objects.get_or_create(user=user, learning_task_id=learning_task_id)
        if not created:
            if inprogress.value == 'Select':
                inprogress.value = 'Unselect'
            else: 
                inprogress.value = 'Select'
        inprogress.save()
    return redirect('student')

# select function, retreiving learning task ID, 
# if user selecting happy is already associated to the learning task, then upon clicking the button they are removed

def notstarted_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)
        if user in learning_task_obj.notstarted.all():
            learning_task_obj.notstarted.remove(user)
        else:
            learning_task_obj.notstarted.add(user)
        notstarted, created = LTNotStarted.objects.get_or_create(user=user, learning_task_id=learning_task_id)
        if not created:
            if notstarted.value == 'Select':
                notstarted.value = 'Unselect'
            else: 
                notstarted.value = 'Select'
        notstarted.save()
    return redirect('student')


# select function, retreiving learning task ID, 
# if user selecting happy is already associated to the learning task, then upon clicking the button they are removed
def needhelp_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)
        if user in learning_task_obj.needhelp.all():
            learning_task_obj.needhelp.remove(user)
        else:
            learning_task_obj.needhelp.add(user)
        needhelp, created = LTNeedHelp.objects.get_or_create(user=user, learning_task_id=learning_task_id)
        if not created:
            if needhelp.value == 'Select':
                needhelp.value = 'Unselect'
            else: 
                needhelp.value = 'Select'
        needhelp.save()
    return redirect('student')

# select function, retreiving learning task ID, 
# if user selecting happy is already associated to the learning task, then upon clicking the button they are removed

def complete_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)
        if user in learning_task_obj.complete.all():
            learning_task_obj.complete.remove(user)
        else:
            learning_task_obj.complete.add(user)
        complete, created = LTComplete.objects.get_or_create(user=user, learning_task_id=learning_task_id)
        if not created:
            if complete.value == 'Select':
                complete.value = 'Unselect'
            else: 
                complete.value = 'Select'
        complete.save()
    return redirect('student')


def complete_percentage(request):
    user = request.user 
    learning_task_id = request.POST.get('learning_task_id')
    learning_task_obj = Learning_Task.objects.get(id=learning_task_id)
    if user in learning_task_obj.complete.all():
         complete = learning_task_obj.complete.all.count()
    complete_count = complete.count()
    context = {
        'complete': complete,
        'complete_count' : complete_count
    }
    return render (request, 'teacher.html', context)
    