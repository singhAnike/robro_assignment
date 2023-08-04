from students_details.models import Student, Course

def create_student(name:str, age:int, course:Course) -> Student:
    student = Student.objects.create(
    name=name,
    age=age,
    course=course,
    )
    return student
def update_student(student: Student, name:str, age:int, course:Course) -> Student:
    student.name=name
    student.age=age
    student.course=course

    student.save()
    return student
def delete_student(student: Student) -> None:
    student.delete()
    return