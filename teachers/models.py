# from django.db import models
# from users.models import ClassRoom, Student

# class Attendance(models.Model):
#     """ Attendance Table"""

#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
#     date = models.DateField()
#     present = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.student} - {self.date}"
