from django.db import models
from users.models import ClassRoom, CustomUser, ClassroomFullError, Bus
from django.dispatch import receiver
from django.db.models.signals import post_save

	
class Student(models.Model):
    """Student Table"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    residence = models.CharField(max_length=20)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.first_name + " " + self.last_name
    
# @receiver(post_save, sender=Student)
# def allocate_bus(sender, instance, created, **kwargs):
#     if created:
#         student_residence = instance.residence
#         buses_in_zone = Bus.objects.filter(zone=student_residence)

#         if buses_in_zone.exists():
#             # Assign the first available bus to the student
#             instance.bus = buses_in_zone.first()
#             instance.save()

    
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
