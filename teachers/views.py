# from django.shortcuts import render
# from django.views.generic.base import View
# from .forms import AttendanceForm


# class AddAttendance(View):
#     template_name = 'add_attendance.html'
#     form_class = AttendanceForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'successful.html')
#         return render(request, self.template_name, {'form': form})