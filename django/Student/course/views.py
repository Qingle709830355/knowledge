from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.core.urlresolvers import reverse

from course.models import Course
from stu.models import Student, StuCourse
from grade.models import Grade


# Create your views here.
def add_course(request):
    """添加课程信息"""
    if request.method == 'GET':
        return render(request, 'addcourse.html')

    if request.method == 'POST':
        c_name = request.POST.get('name')
        c_desc = request.POST.get('desc')
        Course.objects.create(c_name=c_name, c_desc=c_desc)
        return HttpResponseRedirect('/course/allcourse')


def all_course(request):
    """查询所有课程信息"""
    page_id = request.GET.get('page_id', 1)
    course = Course.objects.all()
    paginator = Paginator(course, 3)
    page = paginator.page(int(page_id))
    return render(request, 'allcourse.html', {'courses': page})


def del_course(request, id):
    """删除课程信息"""
    Course.objects.get(id=id).delete()
    return HttpResponseRedirect('/course/allcourse')


def change_course(request, id):
    """修改选中的学生信息"""
    if request.method == 'GET':
        course = Course.objects.get(id=id)
        return render(request, 'changecourse.html', {'course': course})

    if request.method == 'POST':
        course = Course.objects.get(id=id)
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        course.c_name = name
        course.c_desc = desc
        course.save()
        return HttpResponseRedirect('/course/allcourse')


def select_course(request):
    """通过学号或者名字进行模糊查询"""
    if request.method == 'POST':
        str1 = request.POST.get('str1')
        page_id = request.GET.get('page_id', 1)
        # 判断是否只有数字组成，True代表为学号
        if not str(str1).isdigit():
            courses = Course.objects.filter(c_name__contains=str1)
        else:
            courses = Course.objects.filter(c_name__contains=str1)
        paginator = Paginator(courses, 3)
        page = paginator.page(int(page_id))
        return render(request, 'selectcourse.html', {'courses': page, 'str1': str1})


def choice_course(request):
    if request.method == 'GET':
        s_name = request.session['s_name']

        if s_name:
            page_id = request.GET.get('page_id', 1)
            course = Course.objects.all()
            paginator = Paginator(course, 3)
            page = paginator.page(int(page_id))
            s_name = request.session['s_name']
            stu = Student.objects.get(s_name=s_name)
            stucourses = stu.c.all()
            return render(request, 'choicecourse.html', {'courses': page, 'stucourses': stucourses})


def sure_choice(request):
    """确认选择"""
    if request.method == 'GET':
        course_id = request.GET.get('course_id')
        s_name = request.session['s_name']
        if s_name:
            stu = Student.objects.get(s_name=s_name)
            course = Course.objects.get(pk=course_id)
            if stu.c.all().exists():
                return HttpResponseRedirect('/course/choicecourse')
            else:
                stu.c.add(course)
            return HttpResponseRedirect('/course/choicecourse')


def cancle(request):
    """取消选择"""
    if request.method == 'GET':
        course_id = request.GET.get('course_id')
        course = Course.objects.get(id=course_id)
        s_name = request.session['s_name']
        stu = Student.objects.get(s_name=s_name)
        stu.c.remove(course)
        return HttpResponseRedirect('/course/choicecourse')


def ajax_choice(request):
    if request.method == 'GET':
        data = {
            'msg': '请求成功！',
            'coding': 200
        }
        course_id = request.GET.get('course_id')
        s_name = request.session['s_name']
        if s_name:
            stu = Student.objects.get(s_name=s_name)
            course = Course.objects.get(pk=course_id)
            if stu.c.filter(id=course.id).exists():
                data['msg'] = '已经选课该课程！'
            else:
                stu.c.add(course)
                StuCourse.objects.create(student_id=stu.id, course_id=course.id)
                courses = stu.c.all()
                courses = serializers.serialize('json', courses)
                data['courses'] = courses
            return JsonResponse(data)


def ajax_cancle(request):
    if request.method == 'GET':
        data = {
            'msg': '请求成功！',
            'coding': 200
        }
        course_id = request.GET.get('course_id')
        course = Course.objects.get(id=course_id)
        s_name = request.session['s_name']
        if s_name:
            stu = Student.objects.get(s_name=s_name)
            StuCourse.objects.get(student_id=stu.id, course_id=course.id).delete()
            stu.c.remove(course)
            courses = stu.c.all()
            courses = serializers.serialize('json', courses)
            data['courses'] = courses
            return JsonResponse(data)


def all_stucourse(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        return render(request, 'all_stucourse.html', {'grades': grades})


def current_grade_stus(request, g_id):
    """查询当前班级的所有学生"""
    if request.method == 'POST':
        g_name = request.POST.get('grade')
        grade = Grade.objects.get(g_name=g_name)
        stus = grade.student_set.all()
        return render(request, 'currentgradestus.html', {'stus': stus})
    if request.method == 'GET':
        grade = Grade.objects.get(pk=g_id)
        stus = grade.student_set.all()
        return render(request, 'currentgradestus.html', {'stus': stus})


def sure_scores(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        stu_id = request.POST.get('stu_id')
        stu = Student.objects.get(pk=stu_id)
        g_id = stu.g_id
        course_id_score = request.POST.get('score_'+course_id)
        stucourse = StuCourse.objects.get(course_id=course_id, student_id=stu_id)
        stucourse.score = int(course_id_score)
        stucourse.save()
        return HttpResponseRedirect(reverse('course:currentgs', kwargs={'g_id': g_id}))


def select_scores(request):
    if request.method == 'GET':
        s_name = request.session['s_name']
        stu = Student.objects.get(s_name=s_name)
        stucourses = stu.stucourse_set.all()
        return render(request, 'selscores.html', {'stucourses': stucourses, 'stu': stu})
