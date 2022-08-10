from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('student/', views.student, name="student"),
    path('teacher/', views.teacher, name="teacher"),
    path('li/', views.li, name="li"),
    path('learning_intention/', views.learning_intention, name='learning_intention'),
    path('happy_select/', views.happy_select, name='happy_select'),
    path('unsure_select/', views.unsure_select, name='unsure_select'),
    path('sad_select/', views.sad_select, name='sad_select'),
]