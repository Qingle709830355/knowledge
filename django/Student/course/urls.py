from django.conf.urls import url
from course import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()


urlpatterns = [
    url(r'addcourse/', views.add_course, name='addc'),
    url(r'allcourse/', views.all_course, name='allc'),
    url(r'delcourse/(\d+)/', views.del_course, name='delc'),
    url(r'selcourse/', views.select_course, name='selc'),
    url(r'changecourse/(\d+)/', views.change_course, name='changec'),
    url(r'choicecourse/', views.choice_course, name='choice'),
    url(r'surechoice/', views.sure_choice),
    url(r'^nomalcancle/', views.cancle),
    url(r'ajaxchoice/', views.ajax_choice),
    url(r'ajaxcancle/', views.ajax_cancle),
    url(r'allstucourse/', views.all_stucourse),
    url(r'currentgradestus/(?P<g_id>\d+)/', views.current_grade_stus, name='currentgs'),
    url(r'surescores/', views.sure_scores),
    url(r'selscores/', views.select_scores)
]