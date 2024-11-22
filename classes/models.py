from django.db import models
from users.models import User

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')
    code = models.CharField(max_length=10, unique=True)

class StudentClass(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_classes')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
