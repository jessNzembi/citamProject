from django import forms
from .models import Attendance, Student, ClassRoom
from users.models import CustomUser
from users.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm

class ParentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'id_number', 'email')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'grade', 'parent', 'residence']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = CustomUser.objects.filter(role='Parent')

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = ['date', 'present']
		# fields = ['student', 'classroom', 'present']