from students_details.models import Student, Course
from datetime import date

def create_student(name:str, age:int, course:Course, enrollment_date:date) -> Student:
    student = Student.objects.create(
    name=name,
    age=age,
    course=course,
    enrollment_date=enrollment_date,
    )
    return student

def update_student(student: Student, name:str, age:int, course:Course, enrollment_date:date) -> Student:
    student.name=name
    student.age=age
    student.course=course
    student.enrollment_date=enrollment_date
    student.save()
    return student 

def delete_student(student: Student) -> None:
    student.delete()
    return