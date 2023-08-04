from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_list),
    path('students/chart/', views.student_distribution_chart, name='student_distribution_chart'),
    # path('api/add_student/', views.add_student, name='add_student'),
]
