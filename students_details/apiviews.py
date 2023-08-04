from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Student, Course

from students_details.services.commands import create_student, update_student, delete_student
from students_details.services.queries import get_students

# here i used apiview, paginator 

class StudentApi(APIView):
    paginator = PageNumberPagination()
    class InputSerializer(serializers.ModelSerializer):
        course_id= serializers.PrimaryKeyRelatedField(queryset= Course.objects.all())
        class Meta:
            model = Student
            fields = ['name', 'age', 'course_id']
    class OutputSerializer(serializers.ModelSerializer):
        student_id = serializers.IntegerField(source="id")

        class Meta:
            model = Student
            fields = ['student_id', 'name', 'age', 'course_id']

    def get(self, request, *args, **kwargs):
        if 'student_id' in self.kwargs:
            student = get_object_or_404(Student, id=self.kwargs['student_id'])
            serializer = self.OutputSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        students = get_students()
        no_pagination = request.GET.get('no_pagination', False) == 'true'
        if no_pagination:
            return Response(self.OutputSerializer(students, many=True, context={'request': request}).data,
                            status=status.HTTP_200_OK)
        self.paginator.page_size = request.GET.get('count', 10)
        result_page = self.paginator.paginate_queryset(students, request)
        serializer = self.OutputSerializer(result_page, many=True, context={'request': request})
        return self.paginator.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course= serializer.validated_data.pop(
            'course_id') if 'course_id' in serializer.validated_data else None
        student = create_student(course=course, **serializer.validated_data)
        return Response(self.OutputSerializer(student).data, status=status.HTTP_201_CREATED)
    
    def put(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id)
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course= serializer.validated_data.pop(
            'course_id') if 'course_id' in serializer.validated_data else None
        student = update_student(student=student, course=course, **serializer.validated_data)
        return Response(self.OutputSerializer(student).data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id)
        delete_student(student=student)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
