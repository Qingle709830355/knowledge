from django.shortcuts import render
import logging
from rest_framework import mixins, viewsets

from grade.models import Grade, Major
from grade.serializers import GradeSerializer


# Create your views here.
class GradeEdit(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    # 查询所有序列信息
    queryset = Grade.objects.all()
    # 序列化
    serializer_class = GradeSerializer




