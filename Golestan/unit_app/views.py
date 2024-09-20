from django.shortcuts import render
from .forms import LessonForm
from .models import Lesson

def lessonlist(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson_list.html', {'lessons': lessons})