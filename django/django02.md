---
title: Django模型详解
---

[TOC]

# 1.模型设计

在进行模型设计之前，需要将Django的DATABASE配置好，在这里我们将使用到的数据库为mysql，使用之前请先安装pymysql

	pip install pymysql

之后，进行如下配置:

/blogdjango/__init__.py:
	import pymysql
	
	
	pymysql.install_as_MySQLdb()

/blogdjango/setting.py:

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'HOST': 'localhost',
	        'USER': 'root',
	        'PASSWORD': '123456',
	        'PORT': '3306',
	        'NAME': 'myblogdb',
	    }
	}
数据库配置好之后：

/App/models.py:
	
	from django.db import models
	
	
	# Create your models here.
	class BaseModel(object):
	    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
	    update_time = models.DateTimeField(auto_now=True)  # 更新时间
	
	
	class Menu(BaseModel, models.Model):
	    m_name = models.CharField(max_length=30)
	
	    class Meta:
	        db_table = 'menu'
	
	
	class AboutMe(BaseModel, models.Model):
	    name = models.CharField(max_length=32)
	    desc = models.CharField(max_length=256, null=True, blank=True)
	    avatar = models.CharField(max_length=256, null=True, blank=True)
	
	    class Meta:
	        db_table = 'about_me'
	
	    def to_dict(self):
	        return {
	            'pk': self.id,
	            'name': self.name,
	            'desc': self.desc,
	            'avatar': self.avatar
	        }
	
	
	class MyImg(BaseModel, models.Model):
	    m_img = models.CharField(max_length=256)
	
	    class Meta:
	        db_table = 'my_img'
	
	
	class ArticleType(BaseModel, models.Model):
	    typename = models.CharField(max_length=32)
	    num = models.IntegerField(default=0)
	
	    class Meta:
	        db_table = 'article_type'
	
	    def to_dict(self):
	        return {
	            'pk': self.id,
	            'typename': self.typename,
	            'num': self.num
	        }
	
	
	class Article(BaseModel, models.Model):
	    a_title = models.CharField(max_length=128)
	    a_content = models.TextField()
	    hot_point = models.IntegerField(default=0)
	    title_img = models.CharField(max_length=128, null=True, blank=True)
	    type = models.ForeignKey(ArticleType, null=True, blank=True)
	
	    class Meta:
	        db_table = 'article'
	
	    def to_dict(self):
	        return {
	            'pk': self.pk,
	            'a_title': self.a_title,
	            'a_content': self.a_content,
	            'title_img': self.title_img,
	            'type': self.type.typename if self.type != None else self.type,
	            'hot_point': self.hot_point
	        }
	
	
	class RecommendArticle(BaseModel, models.Model):
	    article = models.ForeignKey(Article)
	
	    class Meta:
	        db_table = 'recommend_article'
	
	    def to_dict(self):
	        return {
	            'article_id': self.article.id,
	            'article': self.article.a_title
	        }
	
	
	class LabelCloud(BaseModel, models.Model):
	    label_name = models.CharField(max_length=32)
	
	    class Meta:
	        db_table = 'label_cloud'
	
	
	class Message(BaseModel, models.Model):
	    email = models.EmailField(max_length=64, null=True, blank=True)
	    qq = models.CharField(max_length=20, null=True, blank=True)
	    weixin = models.CharField(max_length=64, null=True, blank=True)
	    content = models.TextField()
	    nickname = models.CharField(max_length=64)
	    is_comment = models.IntegerField()
	    article = models.ForeignKey(Article, null=True, blank=True)
	
	    class Meta:
	        db_table = 'message'

上述模型是我在写个人博客项目时所设计的模型，不过在过程中发现我所设置的基础类BaseModel在进行数据迁移后并不能创建基础类中所描述的字段。 模型中的to_dict方法是为了方便些接口，而进行的转化成字典形式的操作

模型设计好了之后，可以通过以下操作进行数据迁移

	python manage.py makemigrations
	python manage.py migrate

注意：在进行数据迁移操作时，将会遇到很多问题，我将在django补充中把我遇到的问题以及解决方法一一列出

# 2. 模型关联设计

## 2.1 一对一
在数据库模型设计的时候，一对一的情况其实是很少的，在这里举例桌子与学生的对应关系, 一张桌子可以对应一个学生，一个学生对应一个桌子，学生与桌子的关系即为一对一。

student模型：

	class Student(models.Model):
		s_name = models.CharField(max_length=30)
		class Meta:
			db_table = 'stu'

table模型:

	class Table(models.Model):
		stu = OneToOneField(Student)
		class Meta:
			db_table = 'table'
当有了桌子的对象后，可以直接通过table.stu.s_name查找学生的名字
当有了学生的对象后，可以直接通过stu.table.id查找到桌子的id

## 2.2 一对多
一对多这个关系，在现实生活中是最多的，一个作者可以对应多篇文章，一篇文章对应一个作者（当然也有可能有两个作者的情况，但在这里不考虑), 在这里我举例一个我的个人博客项目中的一个一对多的关系

文章模型：

	class Article(BaseModel, models.Model):
	    a_title = models.CharField(max_length=128)
	    a_content = models.TextField()
	    hot_point = models.IntegerField(default=0)
	    title_img = models.CharField(max_length=128, null=True, blank=True)
	    type = models.ForeignKey(ArticleType, null=True, blank=True)
	
	    class Meta:
	        db_table = 'article'
	
	    def to_dict(self):
	        return {
	            'pk': self.pk,
	            'a_title': self.a_title,
	            'a_content': self.a_content,
	            'title_img': self.title_img,
	            'type': self.type.typename if self.type != None else self.type,
	            'hot_point': self.hot_point
	        }

文章类别模型：

	class ArticleType(BaseModel, models.Model):
	    typename = models.CharField(max_length=32)
	    num = models.IntegerField(default=0)
	
	    class Meta:
	        db_table = 'article_type'
	
	    def to_dict(self):
	        return {
	            'pk': self.id,
	            'typename': self.typename,
	            'num': self.num
	        }
当有了文章对象的时候，若文章的type_id字段不为空，可以通过article.articletype.typename查询到该文章的类别名称

当有了文章类别，可以通过type.article_set.all()查找到所有该类别下的文章。

## 2.3 多对多

### A. 在数据库表中的多对多,有两种方式:
方式1 – 自定义第三张表

	class B2G(models.Model):
	    b_id = models.ForeignKey('Boy')
	    g_id = models.ForeignKey('Girl')
	
	class Boy(models.Model):
	        name = models.CharField(max_length=16)
	
	class Girl(models.Model):
	    name = models.CharField(max_length=16)

方式2 –使用models中自带的ManytoManyField自动创建第三张表
	
	class Boy(models.Model):
	    name = models.CharField(max_length=16)
	
	class Girl(models.Model):
	    name = models.CharField(max_length=16)
	    b = models.ManyToManyField('Boy')  
注：使用多对多自动创建后,会创建第三张表,第三张表中会将操作的前两张表中的ID做对应

### B.多对多查询
		
	#正向查询
	#获取一个女孩对象
	
	g1 = Girl.objects.get(id=1)
	
	#获取和当前女孩有关联的所有男孩
	g1.b.all()  #获取全部
	
	#反向查询
	b1 = Boy.objects.get(id=1)
	b1.girl_set.all() #获取全部
	
	#连表查询
	#正向连表
	Girl.objects.all().values('id','name','b__username')
	
	#反向连表
	Boy.objects.all().values('id','name','girl__name')
	#注意此处为girl__name,并非girl_set__name.


