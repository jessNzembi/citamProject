from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Bus

@receiver(post_save, sender=Student)
def allocate_bus(sender, instance, created, **kwargs):
    if created:
        student_residence = instance.residence
        buses_in_zone = Bus.objects.filter(zone=student_residence)

        if buses_in_zone.exists():
            # Assign the first available bus to the student
            instance.bus = buses_in_zone.first()
            instance.save()
