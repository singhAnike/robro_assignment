from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from .models import Student
import os
from django.db.models import Count

def students_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# def student_distribution_chart(request):
#     students = Student.objects.all()
#     course_counts = students.values('course').annotate(count=Count('id'))
#     df = pd.DataFrame(list(course_counts))
#     plt.bar(df['course'], df['count'])
#     plt.xlabel('Course')
#     plt.ylabel('Number of Students')
#     plt.title('Distribution of Students across Courses')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     chart_image = 'student_distrubution_chart.png'
#     plt.savefig(f'students_details/static/{chart_image}')
#     plt.close()
#     return render(request, 'student_distribution_chart.html', {'chart_image': chart_image})




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

