from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from .models import CustomUser, Teacher, Parent
from django.utils import timezone
from .forms import CustomUserCreationForm, TeacherCreationForm
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
        role = request.POST.get('role')
        if role == 'admin':
            user = CustomUser.objects.filter(email=request.POST.get('email'))
            if user:
                if user[0].check_password(request.POST.get('password')):
                    user[0].last_login = timezone.now()
                    user[0].save()
                    
                    return render(request, 'admin_dash.html')
        if role == 'parent':
            user = Parent.objects.filter(email=request.POST.get('email'))
            if user:
                if user[0].check_password(request.POST.get('password')):
                    user[0].last_login = timezone.now()
                    user[0].save()
                    
                    return render(request, 'parent_dash.html')
        if role == 'teacher':
            user = Teacher.objects.filter(email=request.POST.get('email'))
            if user:
                if user[0].check_password(request.POST.get('password')):
                    user[0].last_login = timezone.now()
                    user[0].save()
                    
                    return render(request, 'teacher_dash.html')
        messages.add_message(request, messages.INFO, "Invalid Credentials!")
        return render(request, 'registration/login.html')

class AddTeacher(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_teacher.html')
    
    def post(self, request, *args, **kwargs):
        # data = {
        #     'first_name': request.POST.get('first_name'),
        #     'last_name': request.POST.get('last_name'),
        #     'email': request.POST.get('email'),
        #     'password': request.POST.get('password'),
        #     'phone_number': request.POST.get('phone_number'),
        #     'id_number': request.POST.get('id_number'),
        #     'role': request.POST.get('role')
        # }
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        id_number = request.POST.get('id_number')
        #role = request.POST.get('role')

        teacher = Teacher()
        #teacher.set_password = request.POST.get('password')

        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.email = email
        teacher.password = make_password(password)
        teacher.phone_number = phone_number
        teacher.id_number = id_number
        teacher.role = 'teacher'
        teacher.save()

        #erick = CustomUser.objects.filter(first_name='Erick')
        #print(erick[0].role)
        return render(request, 'successful.html')
    
    
