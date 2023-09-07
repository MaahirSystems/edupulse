from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, StudentForm, TeacherForm

def create_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('some_redirect_view')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'engagement/add-student.html', {'user_form': user_form, 'student_form': student_form})

# Similarly for other roles like create_teacher, create_admin, etc.
