
---
title: python学习记录 使用cmd的第一个Django项目！
---

# 什么是Django？
Django是一个用Python编写的开放源代码的Web应用框架，代码是开源的。此系统采用了MVC的框架模式, 也可以称为MTV模式。


不过MVC和MVT的总体内容是一样的，都是模型，控制， 视图三层结构，但是MVC是： M(model/模型层) V(view/视图层) C(controller/控制层), 二MTV是：M(model/模型层), T(Template/视图层), V(view/处理业务逻辑, 和controller相似)

# 一、在控制台中安装virtualenv虚拟环境
virtualenv使用场景:当开发成员负责多个项目的时候，每个项目安装的库又是有很多差距的时候，会使用虚拟环境将每个项目的环境给隔离开来。
## 1. 安装virtualenv
```
pip install virtualenv
```
## 2. 新建一个虚拟环境
```
virtualenv --no-site-package 文件名
```
注意：在建立虚拟环境是一定要选择好路径，这个虚拟环境以后可能会多次使用，要是忘记再哪了，再重新创建一个和这个虚拟环境一样的还是比较麻烦的

## 3. 进入虚拟环境
```
cd Scripts
```
首先要进入虚拟环境中的Scripts文件夹中
```
activate
```

![img](https://img-blog.csdn.net/20180423185258522?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

出现上图的场景时，就代表您已经进入了名字为testenv的虚拟环境了，也可以使用deativate退出当前的虚拟环境


# 二、安装Django并运行(都在虚拟环境中进行)
## 1. 安装
```
pip install django==<版本号>
```
注：要是不填写版本号，默认最新版本
## 2. 建立一个Django项目
```
django-admin startproject 项目名
```
在虚拟环境中你可以使用cd 命令进入任何一个您想要进入的文件夹， 建立您的Django项目

![img](https://img-blog.csdn.net/20180423190313433?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
这就是我们建立的第一个Django项目

进入文件夹，看看里面有什么东西，您也可以直接打开计算机中的该目录

![img](https://img-blog.csdn.net/20180423190527577?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

firstDjango里面：
![img](https://img-blog.csdn.net/20180423190553755?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


## 3. 运行这个初始的Django项目
```
python manage.py runserver 端口
```
注：也可以不写端口，默认端口为8000

出现下面的效果时，就代表运行成功，这个时候就可以输入127.0.0.1:'您设置的端口号'

![img](https://img-blog.csdn.net/20180423191234277?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


![img](https://img-blog.csdn.net/20180423191245574?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

也可以通过修改firstDjango文件中的setting.py文件中的LANGUAGE_CODE 的值，可以直接把网页渲染成中文

![img](https://img-blog.csdn.net/20180423191255891?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180423191306458?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


# 三、DjangoMTV框架的简单实现

在这个操作里面我使用的一个非常强大的文本编辑器sublime

## 1. 在上面的操作环境中，（正确的虚拟环境下）, 创建一个app(名字自己取)
```
pyhton manage.py startapp 文件名
```

![img](https://img-blog.csdn.net/20180423193012887?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

这是用sublime打开firstDjango，可以看到已经多出了一个文件夹

![img](https://img-blog.csdn.net/20180423193023270?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 2. 添加app进入主项目中

找到firstDjango文件夹下的setting.py，在INSTALLED_APPS里面添加app
![img](https://img-blog.csdn.net/20180423193740763?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


## 2. 在views.py中写入方法处理请求并返回一个页面

```
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def first_hello(request)
	return HttpResponse('hello, world!')

```

## 3. 调用app中的方法
### 1). 在app中先创建一个urls.py文件， 并在里面调用views中的方法
```
# -*- coding:utf-8 -*-
from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'hello', views.first_hello)
]
```
### 2). 在主文件中包括app.urls(firstDjango文件夹中的urls.py)
```
 url(r'app/', include('app.urls')),
```
![img](https://img-blog.csdn.net/20180423195306213?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

最后再次启动服务，输入127.0.0.1:<端口号>/<app名字>/hello 出现以下结果：

![img](https://img-blog.csdn.net/2018042319520667?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 3). 还可以继续建立不同的app,方法都同第二布，也就不再此处详细介绍了

### 4). 连接数据库
进行此部的时候，我们想要模拟增加删除学生信息, 大家可以先自行按照2的方法添加一个学生'app', 先不写方法，把简单的东西配置好！

....

结果图: 

![img](https://img-blog.csdn.net/20180423201420606?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 5). 写添加删除方法
- 在stu文件夹中的model.py里，添加数据模型，也就是建立一个数据表格
```
from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20)
	sex = models.BooleanField()

	class Meta:
		db_table = 'stu'


```

- 在stu文件夹的views.py里， 添加下面内容：
```
from django.shortcuts import render
from django.http import HttpResponse
from stu import models

# Create your views here.

def add_student(request):
	stu = models.Student()
	stu.name = '张三'
	stu.sex = 1
	stu.save()
	return HttpResponse('添加成功！')

def del_student(request):
	# stu = models.Student()
	models.Student.objects.get(name='张三').delete()
	return HttpResponse('删除成功！')


```
注意：这里面有个坑，在删除数据的时候，不能直接用变量名stu， 而需要使用对象名models.Student
- 添加进stu的urls里：
```
from django.conf.urls import url, include
from stu import views

urlpatterns = [
    url(r'addStu/', views.add_student),
    url(r'delStu/', views.del_student)
]
```
- 在主文件的urls.py中包括stu.urls
```
 url(r'stu/', include('stu.urls'))
```

- 配置setting.py , 使之可已连接相关数据库
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  #使用的是mysql数据库
        'HOST': 'localhost', # 本机ip
        'USER': 'root', 
        'PASSWORD': '123456', # 数据库密码
        'NAME': 'firsthello' # 数据库名字
    }
}
```
注意：如果按照上面的配好了直接运行的话，肯定会报错， 因为这个时候，程序还识别不了mysql， 需要在初始方法里，导入pymysql, 即在主文件（firstDjango）中的__init__.py中


```
import pymysql

pymysql.install_as_MySQLdb()

```

### 6). 运行结果：

进入：127.0.0.1:8000/stu/addStu：
![img](https://img-blog.csdn.net/20180423205953126?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

打开数据库查看，stu表中已经多出了一个数据：

![img](https://img-blog.csdn.net/20180423210041224?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

进入：127.0.0.1:8000/stu/delStu:
![img](https://img-blog.csdn.net/20180423210153483?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FneTcwOTgzMDM1NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

打开数据库， 已经将name='张三'的数据删除掉了。






