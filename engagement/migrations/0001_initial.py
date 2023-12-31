# Generated by Django 4.1.7 on 2023-09-14 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credits', models.IntegerField()),
                ('course_code', models.CharField(max_length=10)),
                ('delivery_mode', models.CharField(choices=[('ON', 'Online'), ('BL', 'Blended'), ('FF', 'Face to Face')], default='BL', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engagement.course')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_action', models.CharField(choices=[('NA', 'NA'), ('EC', 'Follow up email and call'), ('PC', 'Pastoral Care'), ('SP', 'Personalised Study Plan/ Extra Session'), ('EM', 'Emergency Contact'), ('OT', 'Other')], default='NA', max_length=2)),
                ('recommended_program_leader_action', models.CharField(blank=True, choices=[('W1', 'Warning Letter - 1'), ('W2', 'Warning Letter - 2')], max_length=2, null=True)),
                ('enrolment_status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('W', 'Withdrawn')], default='A', max_length=2)),
                ('risk_status', models.CharField(choices=[('AR', 'At Risk'), ('NA', 'Not At Risk')], default='NA', max_length=2)),
                ('engagement_status', models.CharField(choices=[('EN', 'Engaged'), ('NE', 'Not Engaged')], default='NE', max_length=2)),
                ('enrollment_date', models.DateField()),
                ('lms_access_date', models.DateField()),
                ('course_offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='engagement.courseoffering')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_international', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyEngagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_status', models.CharField(choices=[('AR', 'At Risk'), ('NA', 'Not At Risk')], default='NA', max_length=2)),
                ('engagement_status', models.CharField(choices=[('EN', 'Engaged'), ('NE', 'Not Engaged')], default='NE', max_length=2)),
                ('enrollement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_engagements', to='engagement.enrollment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_engagements', to='engagement.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campus_teacher', to='engagement.campus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_support', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course_offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='engagement.courseoffering')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='program_leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('program_leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='engagement.programleader')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_developments', to='engagement.campus')),
                ('teachers', models.ManyToManyField(related_name='professional_developments', to='engagement.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_city', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placements', to='engagement.student')),
            ],
        ),
        migrations.CreateModel(
            name='PastoralCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pastoral_care', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OnCampusAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date_time', models.DateTimeField()),
                ('check_out_date_time', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='on_campus_attendances', to='engagement.student')),
            ],
        ),
        migrations.CreateModel(
            name='LabAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campus_lab_assistant', to='engagement.campus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lab_assistant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='engagement.student'),
        ),
        migrations.AddField(
            model_name='courseoffering',
            name='lab_assistants',
            field=models.ManyToManyField(blank=True, related_name='assisting_courses', to='engagement.labassistant'),
        ),
        migrations.AddField(
            model_name='courseoffering',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_offerings', to='engagement.semester'),
        ),
        migrations.AddField(
            model_name='courseoffering',
            name='teachers',
            field=models.ManyToManyField(related_name='teaching_courses', to='engagement.teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='programs',
            field=models.ManyToManyField(related_name='courses', to='engagement.program'),
        ),
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ceo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampusManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='campus_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campus',
            name='campus_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campuses', to='engagement.campusmanager'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=True)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engagement.enrollment')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='engagement.session')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(choices=[('Formative', 'Formative'), ('Summative', 'Summative')], default='Summative', max_length=10)),
                ('score', models.IntegerField()),
                ('grade', models.CharField(max_length=2)),
                ('date', models.DateField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_results', to='engagement.assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_results', to='engagement.student')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='course_offering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='engagement.courseoffering'),
        ),
        migrations.CreateModel(
            name='AdmissionsStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admissions_staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
