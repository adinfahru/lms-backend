from rest_framework import serializers
from .models import Class, StudentClass
from users.serializers import UserSerializer

class StudentClassSerializer(serializers.ModelSerializer):
    student = UserSerializer()  # Menyertakan informasi user (student)
    
    class Meta:
        model = StudentClass
        fields = ['student', 'class_obj']

class ClassSerializer(serializers.ModelSerializer):
    students = StudentClassSerializer(source='studentclass_set', many=True, read_only=True)  # Menyertakan student
    
    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'code', 'students']
