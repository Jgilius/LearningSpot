from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('student/', views.student, name="student"),




    path('teacher/', views.teacher, name="teacher"),







    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('learning_intention/', views.learning_intention, name='learning_intention'),
    path('learning_task/', views.learning_task, name='learning_task'),
    path('happy_select/', views.happy_select, name='happy_select'),
    path('unsure_select/', views.unsure_select, name='unsure_select'),
    path('sad_select/', views.sad_select, name='sad_select'),
    path('inprogress_select/', views.inprogress_select, name='inprogress_select'),
    path('notstarted_select/', views.notstarted_select, name='notstarted_select'),
    path('needhelp_select/', views.needhelp_select, name='needhelp_select'),
    path('complete_select/', views.complete_select, name='complete_select'),
    
]