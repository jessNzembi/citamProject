from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, ClassRoom

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
        model = CustomUser
        fields = '__all__'

class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name', 'grade', 'teacher']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the 'teacher' field if needed
        self.fields['teacher'].queryset = CustomUser.objects.filter(role='Teacher')  # Show all teachers in the dropdown

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['first_name', 'last_name', 'grade', 'parent']