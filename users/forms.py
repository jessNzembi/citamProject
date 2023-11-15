from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Teacher

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'id_number', 'email', 'role')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'id_number', 'email', 'role')

class TeacherCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'