from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_reverse_admin import ReverseModelAdmin
from .models import (
    Admin, CEO, ProgramLeader, Teacher, LabAssistant, Student, 
    Program, Course, Semester, CourseOffering, Session, Enrollment, Attendance
)
# Custom admin for user roles
class AdminAdmin(admin.ModelAdmin):
    list_display = ['user']

class CEOAdmin(admin.ModelAdmin):
    list_display = ['user']

class ProgramLeaderAdmin(admin.ModelAdmin):
    list_display = ['user']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user']

class LabAssistantAdmin(admin.ModelAdmin):
    list_display = ['user']

class StudentAdmin(ReverseModelAdmin):


    list_display = ['user', 'is_international',]
    search_fields = ['user__username', ]
    list_filter = ['is_international', ]

    inline_type = 'stacked'
    inline_reverse = [('user', {'fields': ['username', 'email', 'first_name', 'last_name']})]

# Custom admin for other models
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']

class CourseOfferingAdmin(admin.ModelAdmin):
    list_display = ['course', 'semester']
    list_filter = ['semester']

class SessionAdmin(admin.ModelAdmin):
    list_display = ['course_offering', 'date']
    list_filter = ['course_offering__semester']

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course_offering']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['session', 'enrollment', 'is_present']
    list_filter = ['is_present']
admin.site.register(Admin, AdminAdmin)
admin.site.register(CEO, CEOAdmin)
admin.site.register(ProgramLeader, ProgramLeaderAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(LabAssistant, LabAssistantAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(CourseOffering, CourseOfferingAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
