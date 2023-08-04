from students_details.models import Student

def get_students() -> Student:
    return Student.objects.all()

