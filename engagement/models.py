from django.contrib.auth.models import User
from django.db import models

# User role models
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

class CEO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ceo')

class ProgramLeader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='program_leader')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

class LabAssistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lab_assistant')

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    is_international = models.BooleanField(default=False)
    AT_RISK = 'AR'
    NOT_AT_RISK = 'NA'
    RISK_STATUS_CHOICES = [
        (AT_RISK, 'At Risk'),
        (NOT_AT_RISK, 'Not At Risk'),
    ]
    ENGAGED = 'EN'
    NOT_ENGAGED = 'NE'
    ENGAGEMENT_STATUS_CHOICES = [
        (ENGAGED, 'Engaged'),
        (NOT_ENGAGED, 'Not Engaged'),
    ]
    risk_status = models.CharField(max_length=2, choices=RISK_STATUS_CHOICES, default=NOT_AT_RISK)
    engagement_status = models.CharField(max_length=2, choices=ENGAGEMENT_STATUS_CHOICES, default=NOT_ENGAGED)


# Academic program, courses, and semesters
class Program(models.Model):
    name = models.CharField(max_length=100)
    program_leader = models.ForeignKey(ProgramLeader, on_delete=models.SET_NULL, null=True, related_name='programs')

class Course(models.Model):
    name = models.CharField(max_length=100)
    programs = models.ManyToManyField(Program, related_name='courses')

class Semester(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='course_offerings')
    teachers = models.ManyToManyField(Teacher, related_name='teaching_courses')
    lab_assistants = models.ManyToManyField(LabAssistant, related_name='assisting_courses', blank=True)

class Session(models.Model):
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField()
    
    NA = 'NA'
    EMAIL_CALL = 'EC'
    PASTORAL_CARE = 'PC'
    STUDY_PLAN = 'SP'
    EMERGENCY_CONTACT = 'EM'
    OTHER = 'OT'
    FOLLOW_UP_ACTION_CHOICES = [
        (NA, 'NA'),
        (EMAIL_CALL, 'Follow up email and call'),
        (PASTORAL_CARE, 'Pastoral Care'),
        (STUDY_PLAN, 'Personalised Study Plan/ Extra Session'),
        (EMERGENCY_CONTACT, 'Emergency Contact'),
        (OTHER, 'Other'),
    ]
    follow_up_action = models.CharField(max_length=2, choices=FOLLOW_UP_ACTION_CHOICES, default=NA)
    
    WARNING_1 = 'W1'
    WARNING_2 = 'W2'
    PROGRAM_LEADER_ACTION_CHOICES = [
        (WARNING_1, 'Warning Letter - 1'),
        (WARNING_2, 'Warning Letter - 2'),
    ]
    recommended_program_leader_action = models.CharField(max_length=2, choices=PROGRAM_LEADER_ACTION_CHOICES, blank=True, null=True)
    AT_RISK = 'AR'
    NOT_AT_RISK = 'NA'
    RISK_STATUS_CHOICES = [
        (AT_RISK, 'At Risk'),
        (NOT_AT_RISK, 'Not At Risk'),
    ]
    ENGAGED = 'EN'
    NOT_ENGAGED = 'NE'
    ENGAGEMENT_STATUS_CHOICES = [
        (ENGAGED, 'Engaged'),
        (NOT_ENGAGED, 'Not Engaged'),
    ]
    risk_status = models.CharField(max_length=2, choices=RISK_STATUS_CHOICES, default=NOT_AT_RISK)
    engagement_status = models.CharField(max_length=2, choices=ENGAGEMENT_STATUS_CHOICES, default=NOT_ENGAGED)
# Enrollment and attendance
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name='enrollments')

class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='attendances')
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=True)
