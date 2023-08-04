from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.students_list),
    path('students/chart/', views.student_distribution_chart),
    path('students/enrollment-detailed-chart/', views.students_enrollment_chart),

]
