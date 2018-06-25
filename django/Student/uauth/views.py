from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password

from stu.models import Student


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        role = request.POST.get('role')
        # 如果登录身份是学生的话，可以进行两次判断，首先判断是否存在usernam， 在判断默认账号密码
        if role == 'student':
            if Student.objects.filter(s_username=username).exists():
                stu = Student.objects.filter(s_username=username).first()
                if check_password(password, stu.s_password):
                    request.session['s_name'] = stu.s_name
                    return HttpResponseRedirect('/course/choicecourse')
                else:
                    return render(request, 'login.html', {'message': '用户名不存在！'})
            else:
                if Student.objects.filter(s_num=username).exists():
                    stu = Student.objects.filter(s_num=username)
                    if stu[0].s_num == password:
                        request.session['s_name'] = stu[0].s_name
                        return HttpResponseRedirect('/course/choicecourse')
                    else:
                        return render(request, 'login.html', {'message': '用户名不存在！'})
                else:
                    return render(request, 'login.html', {'message': '用户名不存在！'})
