from django import forms
from .models import *


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'