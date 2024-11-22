from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Class, StudentClass
from .models import Class
from .serializers import ClassSerializer
from .serializers import StudentClassSerializer
from classes.models import Class

class CreateClassView(APIView):
    def post(self, request):
        if request.user.role != 'teacher':
            return Response({'error': 'Only teachers can create classes'}, status=status.HTTP_403_FORBIDDEN)
        
        class_data = request.data
        class_data['teacher'] = request.user.id
        serializer = ClassSerializer(data=class_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JoinClassView(APIView):
    def post(self, request):
        if request.user.role != 'student':
            return Response({'error': 'Only students can join classes'}, status=status.HTTP_403_FORBIDDEN)
        
        class_code = request.data.get('code')
        try:
            class_obj = Class.objects.get(code=class_code)
        except Class.DoesNotExist:
            return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

        student_class = StudentClass.objects.create(student=request.user, class_obj=class_obj)
        return Response({'message': 'Joined class successfully'}, status=status.HTTP_200_OK)

class ClassListView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassStudentListView(APIView):
    def get(self, request, class_id):
        try:
            class_obj = Class.objects.get(id=class_id)
        except Class.DoesNotExist:
            return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

        # Mengambil daftar siswa dengan menggunakan 'students' sebagai related_name
        students = class_obj.students.all()

        # Serialisasi data siswa yang terdaftar
        student_data = StudentClassSerializer(students, many=True)

        return Response(student_data.data, status=status.HTTP_200_OK)