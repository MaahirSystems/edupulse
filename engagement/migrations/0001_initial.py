# Generated by Django 4.2.5 on 2023-09-07 00:06

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
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
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_international', models.BooleanField(default=False)),
                ('risk_status', models.CharField(choices=[('AR', 'At Risk'), ('NA', 'Not At Risk')], default='NA', max_length=2)),
                ('engagement_status', models.CharField(choices=[('EN', 'Engaged'), ('NE', 'Not Engaged')], default='NE', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('follow_up_action', models.CharField(choices=[('NA', 'NA'), ('EC', 'Follow up email and call'), ('PC', 'Pastoral Care'), ('SP', 'Personalised Study Plan/ Extra Session'), ('EM', 'Emergency Contact'), ('OT', 'Other')], default='NA', max_length=2)),
                ('recommended_program_leader_action', models.CharField(blank=True, choices=[('W1', 'Warning Letter - 1'), ('W2', 'Warning Letter - 2')], max_length=2, null=True)),
                ('risk_status', models.CharField(choices=[('AR', 'At Risk'), ('NA', 'Not At Risk')], default='NA', max_length=2)),
                ('engagement_status', models.CharField(choices=[('EN', 'Engaged'), ('NE', 'Not Engaged')], default='NE', max_length=2)),
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
            name='LabAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lab_assistant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='engagement.courseoffering')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='engagement.student')),
            ],
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
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=True)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engagement.enrollment')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='engagement.session')),
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