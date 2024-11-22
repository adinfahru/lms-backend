from django.urls import path
from .views import ClassListView, CreateClassView, JoinClassView, ClassStudentListView

urlpatterns = [
    path('', ClassListView.as_view(), name='class-list'),
    path('classes/<int:class_id>/students/', ClassStudentListView.as_view(), name='class-student-list'), 
    path('create/', CreateClassView.as_view(), name='create-class'),
    path('join/', JoinClassView.as_view(), name='join-class'),
]
