from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Attendance

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = '__all__'