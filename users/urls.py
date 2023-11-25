from django.urls import path
from .views import SignUpView, Login, AddTeacher, Home, AddClassroom, TeacherDashboard

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
	path('teacher_dashboard/<int:teacher_id>/', TeacherDashboard.as_view(), name='teacher_dashboard'),
	path('', Home.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('addTeachers/', AddTeacher.as_view(), name='add_teachers'),
	# path('addParents/', AddParent.as_view(), name='add_parents'),
	path('addClassroom/', AddClassroom.as_view(), name='add_classrooms'),
	# path('addStudent/', AddStudent.as_view(), name='add_students'),
]