from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['student_id', 'lessons']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_id']
