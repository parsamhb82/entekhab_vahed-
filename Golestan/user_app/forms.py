from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['student_id', 'lessons']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_id']
