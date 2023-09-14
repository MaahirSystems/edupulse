from django import forms
from django.contrib.auth.models import User
from .models import Student, Teacher, Admin, CEO, ProgramLeader, LabAssistant

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['is_international']

# Likewise for other roles
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = []
# ... and so on for other roles
