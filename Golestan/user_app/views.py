from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm, StudentForm, TeacherForm

def register_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'register_student.html', {'user_form': user_form, 'student_form': student_form})


def register_teacher(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()

            login(request, user)
            return redirect('some_success_page')

    else:
        user_form = UserForm()
        teacher_form = TeacherForm()

    return render(request, 'register_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form})
