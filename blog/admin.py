from django.contrib import admin
from .models import Arrival_details,Contact


class Arrival_detailsAdmin(admin.ModelAdmin):
    
    list_display = ('new_arrival_title','new_arrival_description','new_arrival_img_url',)

    search_fields =('new_arrival_title','new_arrival_description','new_arrival_img_url',)
    
    list_filter = ()

# Register your models here.
admin.site.register(Arrival_details,Arrival_detailsAdmin)
admin.site.register(Contact)