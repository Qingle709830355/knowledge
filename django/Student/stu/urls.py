from django.conf.urls import url
from stu import views

urlpatterns = [
    url(r'addstu/', views.add_stu, name='add'),
    # url(r'allstu/', views.all_stu, name='all'),
    url(r'delstu/(\d+)/', views.del_stu, name='del'),
    url(r'selstu/', views.select_stu, name='sel'),
    url(r'changestu/(?P<id>\d+)/', views.change_stuinfo, name='change'),
    url(r'group/', views.group_stu),
    url(r'stus/', views.stus),
    url(r'changeadmin/', views.change_admin)
]