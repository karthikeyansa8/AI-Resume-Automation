from django.db import models
from django.utils.text import slugify #---> import for create a text from the given title(eg:iphone11-something)
from django.contrib.auth.models import User


# Create your models here.


class Person_Details(models.Model):
    name  = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100 ,null=True,unique=True)
    phone_number = models.CharField(max_length=13,null=True)
    department = models.CharField(max_length=100)
    about_us = models.TextField(null=True)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    reg_no = models.IntegerField()
    slug = models.SlugField(unique=True)  # --> for creating unique path for indvidual page
    auth_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # img = models.ImageField()
    
    def save(self,*args,**kwargs):         #   ----> This function create a slug from the title and Stores in the DB
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)   

    def __str__(self):
        return self.name   #--> for print the variable for the backend users


class resume_personal_details(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    linkedin = models.URLField(max_length=254,null=True)
    github = models.URLField(max_length=254,null=True)
    img_url = models.ImageField(null=True,upload_to='Resume/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
class Resume_Education(models.Model):
    
    college_name = models.CharField()
    degree = models.CharField()
    cgpa = models.DecimalField(max_digits=3,decimal_places=2)
    hsc_scl_name = models.CharField()
    hsc_marks = models.IntegerField()
    sslc_scl_name = models.CharField()
    sslc_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.college_name+self.degree