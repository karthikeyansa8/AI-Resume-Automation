from django.db import models
from django.utils.text import slugify #---> import for create a text from the given title(eg:iphone11-something)

# Create your models here.


class Arrival_details(models.Model):
    new_arrival_title = models.CharField(max_length=20)
    new_arrival_description = models.TextField()
    new_arrival_img_url = models.CharField(max_length=255,null=True) #--> default length 200
    new_arrival_created_time_date = models.DateTimeField(auto_now_add=True)
    
    # slug = models.SlugField(unique=True)  # --> for creating unique path for indvidual page
    
    # def save(self,*args,**kwargs):            ----> This function create a slug from the title and Stores in the DB
    #     self.slug = slugify(self.new_arrival_title)
    #     super().save(*args,**kwargs)   

    def __str__(self):
        return self.new_arrival_title   #--> for print the variable for the backend users




class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    Message = models.TextField()
    created_time_date = models.DateTimeField(auto_now_add=True)