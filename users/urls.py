from django.urls import path
from .views import SignUpView, Login, AddTeacher

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('addTeachers/', AddTeacher.as_view(), name='add_teachers'),
]