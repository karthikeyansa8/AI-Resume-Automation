from django.contrib import admin
from . models import Person_Details

# Register your models here.

class pdAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'department',
        'role',
        'reg_no',
    ]

admin.site.register(Person_Details,pdAdmin)
