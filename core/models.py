from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    student_name = models.CharField(max_length=255,null=False,blank=False,default="John")
    student_surname = models.CharField(max_length=255,null=False,blank=False,default="Doe")
    student_age = models.IntegerField()
    def __str__(self):
        return f'{self.student_name} {self.student_surname}'

    class Meta:
        db_table = "students"


class Course(models.Model):
    course_name = models.CharField(max_length=255,null=False,blank=False,default="Nothing")
    description = models.TextField(null=False,blank=True)
    difficulty = models.PositiveIntegerField(default=5,validators=[MinValueValidator(1), MaxValueValidator(10)])
    students = models.ManyToManyField("core.Student")
    lecturer = models.ForeignKey("core.Lecturer",on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = "courses"


class Lecturer(models.Model):
    lecturer_name = models.CharField(max_length=255,null=False,blank=False,default="Jane")
    lecturer_surname = models.CharField(max_length=255,null=False,blank=False,default="Doe")
    age = models.IntegerField()
    work_time_years = models.IntegerField()

    def __str__(self):
        return f'{self.lecturer_name} {self.lecturer_surname}'

    class Meta:
        db_table = "lecturers"