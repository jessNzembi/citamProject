from django.shortcuts import render
from django.views.generic.base import View
from .forms import AttendanceForm, StudentForm, ParentCreationForm
from users.models import ClassroomFullError, CustomUser, Bus
from users.views import TeacherDashboard
from .models import Student, Attendance
from django.contrib.auth.hashers import make_password
from django.contrib import messages

class AddParent(View):
    # def get(self, request, *args, **kwargs):
    #     form = ParentCreationForm()
    #     return render(request, 'add_parent.html', {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = ParentCreationForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'successful.html')
    #     else:
    #         for field, errors in form.errors.items():
    #             for error in errors:
    #                 messages.error(request, f"Error in field '{field}': {error}")
    #         return render(request, 'add_parent.html', {'form': form})
    def get(self, request, *args, **kwargs):
        return render(request, 'add_parent.html')
    
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
        user.role = 'Parent'
        user.save()

        return render(request, 'successful.html')

class AddStudent(View):
    template_name = 'add_student.html'
    form_class = StudentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # student = Student()
    #         student_residence = Student().residence
    #         buses_in_zone = Bus.objects.filter(zone__contains=student_residence)

    #         if buses_in_zone.exists():
    #         # Assign the first available bus to the student
    #             Student().bus = buses_in_zone.first()
    #         else:
    #             print("error")

    #         try:
    #             form.save()
    #             # student.save()
    #             return render(request, 'successful.html')
    #         except ClassroomFullError:
    #             messages.add_message(request, messages.INFO, "Clasroom is Full!")
    #             return render(request, self.template_name, {'form': form})
    #     return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
    
        if form.is_valid():
            student = form.save(commit=False)  # Create a student instance but don't save it yet
            student_residence = student.residence
            buses_in_zone = Bus.objects.filter(zone__contains=student_residence)

            if buses_in_zone.exists():
                student.bus = buses_in_zone.first()  # Assign the first available bus to the student
            else:
                print("error")

            try:
                student.save()  # Now save the student instance with the assigned bus
                return render(request, 'successful.html')
            except ClassroomFullError:
                messages.add_message(request, messages.INFO, "Classroom is Full!")
                return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})

# class AddAttendance(View):
#     template_name = 'add_attendance.html'
#     form_class = AttendanceForm
#     class_list = Student.objects.all()
    

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         id = kwargs.get('teacher_id')
#         # teacher = CustomUser.objects.filter(id=teacher_id)
#         return render(request, "add_attendance.html", {'teacher_id': id, 'form': form, "items": self.class_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         teacher_id = kwargs.get('teacher_id')


#         if form.is_valid():
#             form.save()
#             return render(request, 'successful.html')
#         else:
#             print(form.errors)
#         return render(request, "add_attendance.html", {'teacher_id': teacher_id, 'form': form, "items": self.class_list})
class AddAttendance(View):
    template_name = 'add_attendance.html'
    form_class = AttendanceForm

    def get(self, request, *args, **kwargs):
        teacher_id = kwargs.get('teacher_id')
        class_list = Student.objects.filter(grade__teacher__id=teacher_id)
        form = self.form_class()
        return render(request, self.template_name, {'teacher_id': teacher_id, 'form': form, 'items': class_list})

    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('teacher_id')
        class_list = Student.objects.filter(grade__teacher__id=teacher_id)
        form = self.form_class(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            present_student_ids = [int(student_id) for student_id in request.POST.getlist('student')]

            for student in class_list:
                present = student.id in present_student_ids
                Attendance.objects.create(student=student, classroom=student.grade, date=date, present=present)

            return render(request, 'successful.html')


        # Display form errors using messages
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"Error in field '{field}': {error}")

        return render(request, self.template_name, {'teacher_id': teacher_id, 'form': form, 'items': class_list})    