# Generated by Django 5.0.1 on 2024-01-18 15:16

import apps.teacher.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('score', models.FloatField(default=0, verbose_name='Score')),
                ('gender', models.CharField(choices=[('man', 'MAN'), ('woman', 'WOMAN')], default='man', max_length=50, verbose_name='Gender')),
                ('is_valid', models.BooleanField(default=False, verbose_name='Is Valid')),
                ('crated_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('certificate_photo', models.FileField(upload_to='document/certificate/skill', verbose_name='Certificate Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='teacher.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='LevelEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_university', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name University')),
                ('date_of_graduation', models.DateField(verbose_name='Date Of Graduation')),
                ('graduation', models.CharField(choices=[('diploma', 'DIPLOMA'), ("Bachelor's degree", "BACHELOR'S DEGREE"), ("Master's degree", "MASTER'S DEGREE "), ('doctorate degree', 'DOCTORATE DEGREE')], default='diploma', max_length=50, verbose_name='Graduation')),
                ('Academic_discipline', models.CharField(max_length=50, verbose_name='Academic Discipline')),
                ('graduation_image', models.FileField(upload_to='file/certificate/graduation_teacher', verbose_name='graduation image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_education', to='teacher.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Level Of Education',
                'verbose_name_plural': 'Levels Of Education',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('work_phone', models.CharField(max_length=11, validators=[apps.teacher.validators.validate_credit_work_phone], verbose_name='Work Phone')),
                ('employment_file', models.FileField(upload_to='document/certificate/work', verbose_name='Employment Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to='teacher.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
            },
        ),
    ]
