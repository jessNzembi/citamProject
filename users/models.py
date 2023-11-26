from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib import messages

# role choices
role_choices = (
    ("Pastor", "Pastor"),
    ("Teacher", "Teacher"),
    ("Parent", "Parent"),
)
# grades
grade_choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('8', '7'),
    ('8', '8'),
)

class CustomUser(AbstractBaseUser):
    """user table"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=role_choices, default='Parent')
    id_number = models.BigIntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name + " " + self.last_name

class Bus(models.Model):
    """manages transport"""
    zone_choices = (
        ("Ngong,Kiserian,Rongai", "Ngong,Kiserian,Rongai"),
        ("Karen, Bulbul, Nairobi", "Karen, Bulbul, Nairobi"),
    )
    seats_choices = (
        (14, 14),
        (52, 52),
        (62, 62),
    )
    number_plate = models.CharField(max_length=10, unique=True)
    seats = models.PositiveIntegerField(choices=seats_choices)
    zone = models.CharField(max_length=50, choices=zone_choices)

class Event(models.Model):
    """events table"""
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class ClassRoom(models.Model):
    """classroom Table"""
    grade = models.CharField(max_length=5, choices=grade_choices, null=False, blank=False)
    name = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.grade} {self.name}"
    
class ClassroomFullError(Exception):
    pass
    
# class Student(models.Model):
#     """Student Table"""
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
#     parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
#     residence = models.CharField(max_length=20)

#     def __str__(self):
#         return self.first_name + " " + self.last_name
    
# @receiver(post_save, sender=Student)
# def update_class_capacity(sender, instance, created, **kwargs):
#     """Signal receiver to update class capacity"""
#     if created:
#         if instance.grade.capacity < 50:
#             instance.grade.capacity += 1
#             instance.grade.save()
#         else:
#             raise ClassroomFullError("Classroom is full!")