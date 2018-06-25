from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from stu.models import Student
from grade.models import Grade


# Create your views here.
def add_stu(request):
    """添加学生信息"""
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        grade = Grade.objects.get(id=g_id)
        return render(request, 'addstu.html', {'grade': grade})

    if request.method == 'POST':
        stu_name = request.POST.get('name')
        stu_num = request.POST.get('num')
        g_id = request.POST.get('g_id')
        grade = Grade.objects.get(id=g_id)

        if not Student.objects.filter(s_num=stu_num).exists():
            Student.objects.create(
                s_name=stu_name,
                s_num=stu_num,
                g_id=g_id
            )

            return render(request, 'addstu.html', {'grade': grade})
        else:
            return render(request, 'addstu.html', {'message': '该学号已经存在！'})


# def all_stu(request):
#     """查询所有学生"""
#     if request.method == "GET":
#         page_id = request.GET.get('page_id', 1)
#         stus = Student.objects.all()
#         paginator = Paginator(stus, 3)
#         page = paginator.page(int(page_id))
#         return render(request, 'allstu.html', {'stus': page})


def del_stu(request, id):
    """删除选中的学生"""
    Student.objects.get(id=id).delete()
    g_id = request.GET.get('g_id')
    return HttpResponseRedirect('/stu/allstu', {'g_id': g_id})


def select_stu(request):
    """通过学号或者名字进行模糊查询"""
    if request.method == 'POST':
        str1 = request.POST.get('str1')
        page_id = request.GET.get('page_id', 1)
        # 判断是否只有数字组成，True代表为学号
        if str(str1).isdigit():
            stus = Student.objects.filter(s_num__contains=str1)
        else:
            stus = Student.objects.filter(s_name__contains=str1)
        paginator = Paginator(stus, 3)
        page = paginator.page(int(page_id))
        return render(request, 'selectstu.html', {'stus': page, 'str1': str1})


def change_stuinfo(request, id):
    """修改选中的学生信息"""
    if request.method == 'GET':
        stu = Student.objects.get(id=id)
        return render(request, 'changestu.html', {'stu': stu})

    if request.method == 'POST':
        stu = Student.objects.get(id=id)
        name = request.POST.get('name')
        num = request.POST.get('num')
        stu.s_name = name
        stu.s_num = num
        stu.save()
        return HttpResponseRedirect('/stu/allstu')


def group_stu(request):
    """按专业班级查询学生"""
    if request.method == 'GET':

        return render(request, 'index.html')


def stus(request):
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        page_id = request.GET.get('page_id', 1)
        grade = Grade.objects.get(id=g_id)
        stus = Student.objects.filter(g_id=g_id)
        paginator = Paginator(stus, 3)
        page = paginator.page(int(page_id))
        return render(request, 'allstu.html', {'stus': page, 'grade': grade})
    if request.method == 'POST':
        g_name = request.POST.get('data')
        grade = Grade.objects.get(g_name=g_name)
        stus = Student.objects.filter(g_id=grade.id)
        paginator = Paginator(stus, 3)
        page = paginator.page(1)
        return render(request, 'allstu.html', {'stus': page, 'grade': grade})


def change_admin(request):
    """更改口令"""
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        s_name = request.session['s_name']
        if s_name:
            username = request.POST.get('username')
            password = request.POST.get('password')
            stu = Student.objects.get(s_name=s_name)
            stu.s_username = username
            stu.s_password = make_password(password)
            stu.save()
        return HttpResponseRedirect('/course/choicecourse')
