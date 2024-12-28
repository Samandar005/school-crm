from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('image', 'first_name', 'last_name', 'group', 'date_of_birth', 'telephone_number', 'address')

admin.site.register(Student, StudentAdmin)