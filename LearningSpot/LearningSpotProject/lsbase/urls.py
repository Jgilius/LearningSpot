from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('student/', views.student, name="student"),
    path('teacher/', views.teacher, name="teacher")
]