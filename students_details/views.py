from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from .models import Student
import os
from django.db.models import Count



def students_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_distribution_chart(request):
    students = Student.objects.all()
    course_counts = students.values('course').annotate(count=Count('id'))
    df = pd.DataFrame(list(course_counts))
    plt.bar(df['course'], df['count'])
    plt.xlabel('Course')
    plt.ylabel('Students')
    plt.title('Distribution of Students across Courses')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    chart_image = 'student_distribution_chart.png'

    chart_image_path = os.path.join(static_path, chart_image)
    plt.savefig(chart_image_path)
    plt.close()
    
    return render(request, 'student_distribution_chart.html', {'chart_image_path': 'student_distribution_chart.png'})

def students_enrollment_chart(request):

    students_enrollment = Student.objects.values('course', 'enrollment_date').annotate(count=Count('id'))
    df_students_enrollment = pd.DataFrame(list(students_enrollment))
    pivot_table = df_students_enrollment.pivot(index='enrollment_date', columns='course', values='count').fillna(0)

    plt.figure(figsize=(10, 6))
    for course_name in pivot_table.columns:
        plt.plot(pivot_table.index, pivot_table[course_name], marker='o', label=course_name)

    plt.xlabel('Enrollment Date')
    plt.ylabel('Number of Students')
    plt.title('Number of Students Enrolled in Different Courses Over Time')
    plt.xticks(rotation=45)
    plt.legend()

    chart_image = 'student_enrollment_chart.png'
    static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    chart_image_path = os.path.join(static_path, chart_image)
    plt.tight_layout()
    plt.savefig(chart_image_path)
    plt.close()

    context = {'chart_image': chart_image}

    return render(request, 'student_enrollment_chart.html', context)
