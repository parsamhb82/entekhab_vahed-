from django import forms
from .models import *


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['unit', 'name', 'capacity', 'class_day', 'major', 'start_time', 'end_time']

