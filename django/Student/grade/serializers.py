from rest_framework import serializers

from grade.models import Grade, Major


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['id', 'g_name', 'g_desc']
