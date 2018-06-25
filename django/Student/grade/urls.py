from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from grade import views

router = SimpleRouter()
router.register('grade', views.GradeEdit)

urlpatterns = [

] + router.urls