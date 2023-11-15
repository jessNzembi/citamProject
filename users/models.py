from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

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

class CustomUser(AbstractUser):
    """user table"""

    role_choices = (
        ("Admin", "Admin"),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=role_choices, default='Admin')
    id_number = models.BigIntegerField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Teacher(AbstractBaseUser):
    """Teacher Table"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=role_choices, default='Parent')
    id_number = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Parent(AbstractBaseUser):
    """Parent Table"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=role_choices, default='Parent')
    id_number = models.BigIntegerField(null=True)
    residence = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class ClassRoom(AbstractBaseUser):
    """classroom Table"""
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=5, choices=grade_choices, default='1')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Student(AbstractBaseUser):
    """Student Table"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
    