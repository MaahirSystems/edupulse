from django.urls import path
from .views import create_student

urlpatterns = [
    path('student/add/', create_student, name='create_student'),
    # ... other url patterns
]