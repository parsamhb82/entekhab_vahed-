
from django.shortcuts import render
from .forms import LessonForm
from .models import Lesson
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from user_app.models import Student

def lessonlist(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson_list.html', {'lessons': lessons})



@login_required
def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = request.user.teacher  # Assign the lesson to the logged-in teacher
            lesson.save()
            return redirect('lesson_list')  # Redirect to lesson list after successful creation
    else:
        form = LessonForm()
    return render(request, 'lesson_form.html', {'form': form})

def edit_lesson(request, pk):
    lesson = get_object_or_404(Lesson,pk=pk, teacher=request.user.teacher)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lesson_form.html', {'form': form})

def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk, teacher=request.user.teacher)
    lesson.delete()
    return redirect('lesson_list')



def student_lessons(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    lessons = Lesson.objects.filter(students=student)
    return render(request, 'student_lessons.html', {'lessons': lessons})

def add_lesson_to_student(request, pk):
    student = request.user.student
    lesson = get_object_or_404(Lesson, pk=pk)
    student.lessons.add(lesson)
    return redirect('lesson_list')

def delete_lesson_from_student(request, pk):
    student = request.user.student
    lesson = get_object_or_404(Lesson, pk=pk)
    student.lessons.remove(lesson)
    return redirect('lesson_list')

