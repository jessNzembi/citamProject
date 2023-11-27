from django.shortcuts import render
from django.views.generic.base import View
from .forms import AttendanceForm, StudentForm, ParentCreationForm
from users.models import ClassroomFullError, CustomUser, Bus
from users.views import TeacherDashboard
from .models import Student, Attendance
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
            present_students = form.cleaned_data.get('student', [])  # Assuming your form has a students field

            for student in class_list:
                present = student in present_students
                Attendance.objects.create(student=student, classroom=student.grade, date=date, present=present)

            return render(request, 'successful.html')

        return render(request, self.template_name, {'teacher_id': teacher_id, 'form': form, 'items': class_list})      