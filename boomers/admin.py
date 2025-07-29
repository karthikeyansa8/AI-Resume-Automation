from django.contrib import admin
from . models import Person_Details,resume_personal_details,Resume_Education

# Register your models here.

class pdAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'department',
        'role',
        'reg_no',
    ]

admin.site.register(Person_Details,pdAdmin)
admin.site.register(resume_personal_details)
admin.site.register(Resume_Education)
