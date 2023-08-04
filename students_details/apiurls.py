from django.urls import path
from students_details import apiviews

urlpatterns=[
    path('api/students/', apiviews.StudentApi.as_view()),
    path('api/students/<int:student_id>/', apiviews.StudentApi.as_view()),
]