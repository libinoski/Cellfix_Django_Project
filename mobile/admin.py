from django.contrib import admin
from .models import Customer, Mechanic, Request, Attendance, Feedback

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_name', 'address', 'mobile')

class MechanicAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_name', 'address', 'mobile', 'skill', 'salary', 'status')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('mobile_no', 'mobile_name', 'mobile_model', 'mobile_brand', 'problem_description', 'date', 'cost', 'status')
    list_filter = ('category', 'status', 'mechanic')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('mechanic', 'date', 'present_status')
    list_filter = ('mechanic', 'date', 'present_status')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('date', 'by', 'message')
    list_filter = ('date', 'by')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Mechanic, MechanicAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Feedback, FeedbackAdmin)

