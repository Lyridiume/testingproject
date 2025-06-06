# Generated by Django 5.1.7 on 2025-03-23 17:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer_name', models.CharField(default='Jane', max_length=255)),
                ('lecturer_surname', models.CharField(default='Doe', max_length=255)),
                ('age', models.IntegerField()),
                ('work_time_years', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='student_age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='surname',
        ),
        migrations.AddField(
            model_name='student',
            name='student_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='student_surname',
            field=models.CharField(default='Doe', max_length=255),
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='Nothing', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('students', models.ManyToManyField(to='core.student')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lecturer')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
