from .views import *
from django.urls import path

urlpatterns = [
    path('register/', register_student, name='register'),
    path('login/', register_teacher, name='login'),
]