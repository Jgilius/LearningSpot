from django.http import HttpResponse
from django.shortcuts import redirect

def user_not_authenticated(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('student')
        else: 
            return view_function(request, *args, **kwargs)
    return wrapper_function



def authorised_users(authorised=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in authorised:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page with your current persmissions, please speak to an admin.')
        return wrapper_function
    return decorator



def teacher_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'student':
            return redirect('student')
        if group == 'teacher':
            return view_function(request, *args, **kwargs)
    return wrapper_function
