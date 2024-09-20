from .views import *
from django.urls import path

urlpatterns = [
    path('lesson_list/', lessonlist, name='lesson_list'),
    path('create_lesson/', create_lesson, name='create_lesson'),
    path('edit_lesson/<int:pk>/', edit_lesson, name='edit_lesson'),
    path('delete_lesson/<int:pk>/', delete_lesson, name='delete_lesson'),
    path('add_lesson_to_student/<int:pk>/', add_lesson_to_student, name='add_lesson_to_student'),
    path('delete_lesson_from_student/<int:pk>/', delete_lesson_from_student, name='delete_lesson_from_student'),
]