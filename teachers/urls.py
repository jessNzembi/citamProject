from django.urls import path
from .views import AddAttendance, AddParent, AddStudent

urlpatterns = [
	path('addParents/', AddParent.as_view(), name='add_parents'),
	path('addStudents/', AddStudent.as_view(), name='add_students'),
	path('attendance/', AddAttendance.as_view(), name='attendance'),
]
