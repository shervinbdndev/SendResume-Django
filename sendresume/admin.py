from django.contrib import admin
from .models import SendResumeModel




class SendResumeAdmin(admin.ModelAdmin):
    list_filter = ['fullname' , 'created_at']
    list_display = ['fullname' , 'email' , 'is_read_by_admin']




admin.site.register(SendResumeModel , SendResumeAdmin)