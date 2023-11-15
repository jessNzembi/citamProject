from django.shortcuts import render
from django.views.generic.base import View
from .forms import AttendanceForm
from .models import Attendance
from django.utils.timezone import datetime

class AddAttendance(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_attendance.html', {'form': AttendanceForm()})
    
    def post(self, request, *args, **kwargs):
        
        student = request.POST.get('student')
        teacher = request.POST.get('teacher')
        date = request.POST.get('email')
        present = request.POST.get('present')
        
        attendance = Attendance()

        attendance.student = student
        attendance.teacher = teacher
        attendance.date = date
        attendance.present = present
        
        attendance.save()

        #erick = CustomUser.objects.filter(first_name='Erick')
        #print(erick[0].role)
        return render(request, 'successful.html')
