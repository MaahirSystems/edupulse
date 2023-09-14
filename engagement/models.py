from django.contrib.auth.models import User
from django.db import models

# User role models
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

class CEO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ceo')
class CampusManager(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='campus_manager')
class Campus(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    campus_manager = models.ForeignKey(CampusManager, on_delete=models.SET_NULL, null=True, related_name='campuses')
class ProgramLeader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='program_leader')

class Teacher(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='campus_teacher')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

class LabAssistant(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='campus_lab_assistant')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lab_assistant')

class AdmissionsStaff(models.Model):
    
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admissions_staff')
class PastoralCare(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pastoral_care')
class StudentSupport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_support')
class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    is_international = models.BooleanField(default=False)
   
class Placement(models.Model):
    company_name = models.CharField(max_length=100)
    company_city = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='placements')

# Academic program, courses, and semesters
class Program(models.Model):
    name = models.CharField(max_length=100)
    program_leader = models.ForeignKey(ProgramLeader, on_delete=models.SET_NULL, null=True, related_name='programs')

class Course(models.Model):
    name = models.CharField(max_length=100)
    credits= models.IntegerField()
    course_code = models.CharField(max_length=10)

    ONLINE = 'ON'
    BLENDED = 'BL'
    FACE_TO_FACE = 'FF'
    DELIVERY_MODE = [
        (ONLINE, 'Online'),
        (BLENDED, 'Blended'),
        (FACE_TO_FACE, 'Face to Face')
    ]
    delivery_mode = models.CharField(max_length=2, choices=DELIVERY_MODE, default=BLENDED)
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
    

# Enrollment and attendance

class Enrollment(models.Model):
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
    ACTIVE = 'A'
    INACTIVE = 'I'
    WITHDRAWN = 'W'
    
    ENROLMENT_STATUSES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (WITHDRAWN, 'Withdrawn')
    ]

    enrolment_status = models.CharField(
        max_length=2, 
        choices=ENROLMENT_STATUSES,
        default=ACTIVE
    )
    risk_status = models.CharField(max_length=2, choices=RISK_STATUS_CHOICES, default=NOT_AT_RISK)
    engagement_status = models.CharField(max_length=2, choices=ENGAGEMENT_STATUS_CHOICES, default=NOT_ENGAGED)
    enrollment_date = models.DateField()
    lms_access_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name='enrollments')

class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='attendances')
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=True)

class OnCampusAttendance(models.Model):
    check_in_date_time = models.DateTimeField()
    check_out_date_time = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='on_campus_attendances')
class WeeklyEngagement(models.Model):
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
    enrollement = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='weekly_engagements')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='weekly_engagements')


class ProfessionalDevelopment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='professional_developments')
    teachers = models.ManyToManyField(Teacher, related_name='professional_developments')
class Assessment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name='assessments')
class AssessmentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assessment_results')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='assessment_results')
    FORMATIVE = 'Formative'
    SUMMATIVE = 'Summative'
    
    ASSESSMENT_TYPES = [
        (FORMATIVE, 'Formative'),
        (SUMMATIVE, 'Summative')
    ]

    assessment_type = models.CharField(
        max_length=10, 
        choices=ASSESSMENT_TYPES,
        default=SUMMATIVE
    )
    score = models.IntegerField()
    grade = models.CharField(max_length=2)
    date = models.DateField()
