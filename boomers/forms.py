from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate #---> for checking the username and password
import re
from boomers.models import Resume_Education, resume_personal_details

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username',max_length=30,required=True)
    email = forms.EmailField(label='email',required=True)
    password = forms.CharField(label='password',max_length=10,required=True)
    confirm_password = forms.CharField(label='confirm_password',max_length=10,required=True)
    
    class Meta:   #---> for insert the details in the auth user table 
        model = User
        fields = ['username',
                  'email',
                  'password']
        
    def clean(self):
        cleaned_data = super().clean() 
        email = cleaned_data.get('email')
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if User.objects.filter(email=email):
            raise forms.ValidationError("Email already exists")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("password and confirm password does not match")  #---> for password and confirm password
        
        
class Loginform(forms.Form):
    username = forms.CharField(label='username',max_length=30,required=True)
    password = forms.CharField(label='password', max_length=10,required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username,password=password)
            print('authenticate',user)  # ---> eg karthi39 username

            if user is None:
                raise forms.ValidationError('Invalid username and password')
        
        
class forgot_password_form(forms.Form):
    email = forms.EmailField(label='email',required=True,max_length=254)
    
    def clean(self):
        cleaned_data =  super().clean()
        email = cleaned_data.get('email')
        
        user  = User.objects.filter(email=email).exists()  #--> gives the true or false value
        # print('forms',user)  # ---> gives the username from the DB eg: karthi39
        
        if user is False:
            raise forms.ValidationError('Email id is not registered')
        
        
class Reset_password_form(forms.Form):
    new_password = forms.CharField(label='new_password',max_length=10)
    confirm_password = forms.CharField(label='confirm_password',max_length=10)
    
    def clean(self):
        cleaned_data =  super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password and confirm_password and new_password!=confirm_password:
            raise forms.ValidationError('password and confirm password does not match')
        
class Resume_personal_details_form (forms.ModelForm):
    first_name = forms.CharField(label='first_name',max_length=30,required=True)
    last_name = forms.CharField(label='last_name',max_length=30,required=True)
    email = forms.EmailField(label='email',max_length=30,required=True)
    phone = forms.CharField(label='phone',required=True)
    linkedin = forms.URLField(label='linkedin',required=True)
    github = forms.URLField(label='github',required=True)
    img_url = forms.ImageField(label='img_url',required=False)

    
    class Meta:
        model = resume_personal_details
        fields = ['first_name',
                  'last_name','email','phone','linkedin','github','img_url'
        ]
    
    def clean(self):
        cleaned_data =  super().clean()
        # print(cleaned_data) # ---> {'first_name': 'Karthikeyan', 'last_name': 'S A', 'email': 'karthikeyansa8@gmail.com', 'phone': '+917358996885'}
        email = cleaned_data.get('email')
        check_email =re.match(r'^[a-zA-Z0-9]+@gmail\.com',str(email))
        
        if check_email is None:
            raise forms.ValidationError('Invalid email id')
        
        
        
class Education_form(forms.ModelForm):
    
    college_name = forms.CharField(label='college_name',max_length=255)
    degree = forms.CharField(label='degree',max_length=255)
    cgpa = forms.DecimalField(label='cgpa',max_digits=3,decimal_places=2)
    hsc_scl_name = forms.CharField(label='hsc_scl_name',max_length=255)
    hsc_marks = forms.IntegerField(label='hsc_marks')
    sslc_scl_name = forms.CharField(label='sslc_scl_name',max_length=255)
    sslc_marks = forms.IntegerField(label='sslc_marks')
    
    class Meta:
        model = Resume_Education
        fields = ['college_name',
                  'degree','cgpa','hsc_scl_name','hsc_marks','sslc_scl_name',
                  'sslc_marks'
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)