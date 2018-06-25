from django.db import models


# Create your models here.
class Grade(models.Model):
    """班级"""
    g_name = models.CharField(max_length=30)
    g_desc = models.CharField(max_length=150)

    class Meta:
        db_table = 'grade'


class Major(models.Model):
    """专业"""
    m_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'major'