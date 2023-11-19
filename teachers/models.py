from django.db import models
from users.models import ClassRoom, CustomUser, ClassroomFullError
from django.dispatch import receiver
from django.db.models.signals import post_save

	
class Student(models.Model):
    """Student Table"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    residence = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
@receiver(post_save, sender=Student)
def update_class_capacity(sender, instance, created, **kwargs):
    """Signal receiver to update class capacity"""
    if created:
        if instance.grade.capacity < 50:
            instance.grade.capacity += 1
            instance.grade.save()
        else:
            raise ClassroomFullError("Classroom is full!")

class Attendance(models.Model):
	""" Attendance Table"""

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
	date = models.DateField()
	present = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.student} - {self.date}"
