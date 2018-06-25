from django.db import models


# Create your models here
class Course(models.Model):
    c_name = models.CharField(max_length=30)  # 课程名
    c_desc = models.CharField(max_length=100, null=True, blank=True)  # 添加描述

    class Meta:
        db_table = 'course'


