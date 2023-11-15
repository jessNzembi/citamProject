from django.db import models
from users.models import Teacher, Student

class Attendance():
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
