from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from .models import CustomUser, ClassRoom
from django.utils import timezone
from .forms import CustomUserCreationForm, ClassRoomForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/login.html')
    
    def post(self, request, *args, **kwargs):
        # role = request.POST.get('role')
        # if role == 'pastor':
        user = CustomUser.objects.filter(email=request.POST.get('email'))
        if user:
            if user[0].check_password(request.POST.get('password')):
                user[0].last_login = timezone.now()
                user[0].save()
                if user[0].role == 'Pastor':    
                    return render(request, 'admin_dash.html')
                elif user[0].role == 'Teacher':
                    return redirect('teacher_dashboard', teacher_id=user[0].id)
                elif user[0].role == 'Parent':
                    return render(request, 'parent_dash.html')

        # if role == 'parent':
        #     user = CustomUser.objects.filter(email=request.POST.get('email'))
        #     if user:
        #         if user[0].check_password(request.POST.get('password')):
        #             user[0].last_login = timezone.now()
        #             user[0].save()
                    
        #             return render(request, 'parent_dash.html')
        # if role == 'teacher':
        #     user = CustomUser.objects.filter(email=request.POST.get('email'))
        #     if user:
        #         if user[0].check_password(request.POST.get('password')):
        #             user[0].last_login = timezone.now()
        #             user[0].save()
                    
        #             return render(request, 'teacher_dash.html')
        messages.add_message(request, messages.INFO, "Invalid Credentials!")
        return render(request, 'registration/login.html')

class AddTeacher(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_teacher.html')
    
    def post(self, request, *args, **kwargs):
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        id_number = request.POST.get('id_number')

        user = CustomUser()

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = make_password(password)
        user.phone_number = phone_number
        user.id_number = id_number
        user.role = 'Teacher'
        user.save()

        return render(request, 'successful.html')
    
# class AddParent(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'add_parent.html')
    
#     def post(self, request, *args, **kwargs):
        
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone_number = request.POST.get('phone_number')
#         id_number = request.POST.get('id_number')
#         residence = request.POST.get('residence')

#         parent = Parent()

#         parent.first_name = first_name
#         parent.last_name = last_name
#         parent.email = email
#         parent.password = make_password(password)
#         parent.phone_number = phone_number
#         parent.id_number = id_number
#         parent.role = 'parent'
#         parent.residence = residence
#         parent.save()

#         return render(request, 'successful.html')

class AddClassroom(View):
    def get(self, request, *args, **kwargs):
        form = ClassRoomForm()
        return render(request, 'add_classroom.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'successful.html')
        else:
            return render(request, 'add_classroom.html', {'form': form})

# class AddStudent(View):
#     template_name = 'add_student.html'
#     form_class = StudentForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return render(request, 'successful.html')
#             except ClassroomFullError:
#                 messages.add_message(request, messages.INFO, "Clasroom is Full!")
#                 # return render(request, 'add_student.html')
#         return render(request, self.template_name, {'form': form})
    
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/home.html')
    

class TeacherDashboard(View):
    template_name = 'teacher_dash.html'

    def get(self, request, *args, **kwargs):
        teacher_id = kwargs.get('teacher_id')
        # teacher = get_object_or_404(Teacher, user_id=teacher_id)
        # Retrieve additional data for the teacher dashboard if needed

        return render(request, self.template_name, {'teacher_id': teacher_id})
