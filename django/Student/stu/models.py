from django.db import models
from course.models import Course
from grade.models import Grade, Major


# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=30)
    s_num = models.CharField(max_length=30)
    c = models.ManyToManyField(Course, null=True, blank=True)
    g = models.ForeignKey(Grade, null=True, blank=True)
    m = models.ForeignKey(Major, null=True, blank=True)
    s_username = models.CharField(max_length=30, null=True)
    s_password = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'student'


class StuCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'scores'
