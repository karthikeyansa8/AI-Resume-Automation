from django.db import models
from django.utils.text import slugify #---> import for create a text from the given title(eg:iphone11-something)
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


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
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13,unique=True)
    linkedin = models.URLField(max_length=254,null=True,unique=True)
    github = models.URLField(max_length=254,null=True,unique=True)
    img_url = models.ImageField(null=True,upload_to='Resume/img/')
    district = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
class Resume_Education(models.Model):
    
    college_name = models.CharField( max_length=254)
    college_district = models.CharField(max_length=254)
    college_state = models.CharField(max_length=254)
    degree = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    cgpa = models.CharField(max_length=254)
    cgpa_semester = models.CharField(max_length=254)
    college_passed_out_year = models.CharField(max_length=254)
    hsc_scl_name = models.CharField(max_length=254)
    hsc_scl_district = models.CharField(max_length=254)
    hsc_scl_state = models.CharField(max_length=254)
    hsc_passed_out_year = models.CharField(max_length=254)
    hsc_percentage = models.CharField()
    sslc_scl_name = models.CharField(max_length=254)
    sslc_scl_district = models.CharField(max_length=254)
    sslc_scl_state = models.CharField(max_length=254)
    sslc_passed_out_year = models.CharField(max_length=254)
    sslc_percentage = models.CharField()
    person_id = models.ForeignKey(resume_personal_details, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.college_name+' - ' + self.degree
    

class Resume_Skills(models.Model):
    prog_languages = models.CharField(max_length=254)
    Tools_technologies = models.CharField(max_length=254,null=True)
    person_id = models.ForeignKey(resume_personal_details, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.prog_languages + ' - ' + self.Tools_technologies if self.Tools_technologies else self.prog_languages

class Resume_Projects(models.Model):
    project_count = models.IntegerField(default=0,null=True)  # --> to store the number of projects
    project_name = models.JSONField(null=True)
    project_description = models.JSONField(null=True)
    project_keywords = models.JSONField(null=True)
    person_id = models.ForeignKey(resume_personal_details, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    
class Resume_Internships(models.Model):
    company_name = models.CharField(max_length=254,null=True)
    role = models.CharField(max_length=254,null=True)
    location = models.CharField(max_length=254,null=True)
    duration = models.CharField(max_length=254,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    person_id = models.ForeignKey(resume_personal_details, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
# class Resume_leadership_extracurricular(models.Model):
#     activity_name = models.CharField(max_length=254,null=True)
#     description = models.TextField(null=True)
#     person_id = models.ForeignKey(resume_personal_details, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True,null=True)

class Resume_certifications(models.Model):
    certification_name = ArrayField(models.CharField(max_length=254),default=list,blank=True,null=True)
    person_id = models.ForeignKey(resume_personal_details, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)