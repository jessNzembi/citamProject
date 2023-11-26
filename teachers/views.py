from django.shortcuts import render
from django.views.generic.base import View
from .forms import AttendanceForm, StudentForm, ParentCreationForm
from users.models import ClassroomFullError, CustomUser
from users.views import TeacherDashboard
from .models import Student
from django.contrib import messages

class AddParent(View):
    def get(self, request, *args, **kwargs):
        form = ParentCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ParentCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'successful.html')
        else:
            return render(request, 'signup.html', {'form': form})

class AddStudent(View):
    template_name = 'add_student.html'
    form_class = StudentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'successful.html')
            except ClassroomFullError:
                messages.add_message(request, messages.INFO, "Clasroom is Full!")
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})

class AddAttendance(View):
    template_name = 'add_attendance.html'
    form_class = AttendanceForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        class_list = Student.objects.all()
        teacher_id = kwargs.get('teacher_id')
        # teacher = CustomUser.objects.filter(id=teacher_id)
        return render(request, "add_attendance.html", {'teacher_id': teacher_id, 'form': form, "items": class_list})
        # form = self.form_class()
        # return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # class_list = Student.objects.all()
        # teacher_id = request.GET.get('teacher_id')
        # return render(request, "add_attendance.html", {'teacher_id': teacher_id}, {"items": class_list})
          
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'successful.html')
        return render(request, self.template_name, {'form': form})
        # return render(request, "add_attendance.html", {'teacher_id': teacher_id}, {'form': form}, {"items": class_list})
		
          
        