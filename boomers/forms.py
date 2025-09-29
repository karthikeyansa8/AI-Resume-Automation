from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate #---> for checking the username and password
import re
from boomers.models import Resume_Education, Resume_Internships, Resume_Projects, Resume_Skills, Resume_certifications, resume_personal_details
from django.forms import formset_factory
from django.contrib.postgres.forms import SimpleArrayField


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
    email = forms.EmailField(label='email',required=True)
    
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
    linkedin = forms.URLField(label='linkedin',required=False)
    github = forms.URLField(label='github',required=False)
    district = forms.CharField(label='district',required=True)
    state = forms.CharField(label='state',required=True)
    # img_url = forms.ImageField(label='img_url',required=False)

    
    class Meta:
        model = resume_personal_details
        fields = ['first_name',
                  'last_name','email','phone','linkedin','github','district','state' #, 'img_url'
        ]
    
    def clean(self):
        cleaned_data =  super().clean()
        # print(cleaned_data) # ---> {'first_name': 'Karthikeyan', 'last_name': 'S A', 'email': 'karthikeyansa8@gmail.com', 'phone': '+917358996885'}
        email = cleaned_data.get('email')
        check_email =re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',str(email))
        
        if check_email is None:
            raise forms.ValidationError('Invalid email id')
        
        phone = cleaned_data.get('phone')
        check_phone = re.match(r'^\+?[0-9]{10,13}$',str(phone))
        
        if check_phone is None:
            raise forms.ValidationError('Invalid phone number')
        
        
        return cleaned_data
        
        
        
class Resume_Education_form(forms.ModelForm):
    
    college_name = forms.CharField(label='college_name',max_length=255)
    college_district = forms.CharField(label='college_district')
    college_state = forms.CharField(label='college_state')
    degree = forms.CharField(label='degree',max_length=255)
    branch = forms.CharField(label='branch')
    cgpa = forms.CharField(label='cgpa')
    cgpa_semester = forms.CharField(label='cgpa_semester')
    college_passed_out_year = forms.CharField(label='college_passed_out_year')
    hsc_scl_name = forms.CharField(label='hsc_scl_name',max_length=255)
    hsc_scl_district = forms.CharField(label='hsc_scl_district')
    hsc_scl_state = forms.CharField(label='hsc_scl_state')
    hsc_passed_out_year = forms.CharField(label='hsc_passed_out_year')
    hsc_percentage = forms.FloatField(label='hsc_percentage')
    sslc_scl_name = forms.CharField(label='sslc_scl_name',max_length=255)
    sslc_scl_district = forms.CharField(label='sslc_scl_district')
    sslc_scl_state = forms.CharField(label='sslc_scl_state')
    sslc_passed_out_year = forms.CharField(label='sslc_passed_out_year')
    sslc_percentage = forms.FloatField(label='sslc_percentage')
    
    class Meta:
        model = Resume_Education
        fields = ['college_name','college_district','college_state',
                  'degree','branch','cgpa','cgpa_semester','college_passed_out_year',
                  'hsc_scl_name','hsc_scl_district','hsc_scl_state','hsc_passed_out_year','hsc_percentage',
                  'sslc_scl_name','sslc_scl_district','sslc_scl_state','sslc_passed_out_year','sslc_percentage'
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)
        return cleaned_data
        
class Resume_Skills_form(forms.ModelForm):
    prog_languages = forms.CharField(label='prog_languages',max_length=255)
    Tools_technologies = forms.CharField(label='Tools_technologies',max_length=255,required=False)
    
    class Meta:
        model = Resume_Skills
        fields = ['prog_languages','Tools_technologies']
        
    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)
        return cleaned_data
        
        
        
class Resume_Projects_form(forms.ModelForm):
    project_count = forms.IntegerField(required=False)
    
    class Meta:
        model = Resume_Projects
        fields = ['project_count']

    def __init__(self, *args, **kwargs):
        self.project_count = int(kwargs.pop('project_count', 0))
        super().__init__(*args, **kwargs)
        
        # Add dynamic fields based on project_count
        for i in range(1, self.project_count + 1):
            self.fields[f'project{i}_name'] = forms.CharField(label=f'project{i}_name', max_length=255, required=False)
            
            self.fields[f'project{i}_description'] = forms.CharField(label=f'project{i}_description', widget=forms.Textarea, required=False)
            
            self.fields[f'project{i}_keywords'] = forms.CharField(label=f'project{i}_keywords', max_length=255, required=False)

    def clean(self):
        cleaned_data = super().clean()
        
        # for key , value in cleaned_data.items():
        #     print(f'cleaned_data --> {key} :{value}')  # Debugging line to see cleaned data
            
        self.name = {}
        self.desc = {}
        self.key = {}

        for i in range(1, self.project_count + 1):
            name = cleaned_data.get(f'project{i}_name')
            desc = cleaned_data.get(f'project{i}_description')
            keywords = cleaned_data.get(f'project{i}_keywords')

            # Save only non-empty entries
            if name :
                self.name[f'project{i}_name'] = name
            if desc:    
                self.desc[f'project{i}_description'] = desc
            if keywords:
                self.key[f'project{i}_keywords'] = keywords
    
        return cleaned_data
    
    def save(self, commit=True):
        ins = super().save(commit=False)
        ins.project_name = self.name
        ins.project_description = self.desc
        ins.project_keywords = self.key
        
        if commit and ins.project_name and ins.project_description and ins.project_keywords:
            ins.save()
        
        return ins

class Resume_Internships_form(forms.ModelForm):
    company_name = forms.CharField(label='company_name',max_length=255,required=False)
    role = forms.CharField(label='role',max_length=255,required=False)
    location = forms.CharField(label='location',max_length=255,required=False)
    duration = forms.CharField(label='duration',max_length=255,required=False)
    start_date = forms.DateField(label='start_date',required=False)
    end_date = forms.DateField(label='end_date',required=False)
    
    class Meta:
        model = Resume_Internships
        fields = ['company_name','role','location','duration','start_date','end_date']  
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        
        
# class Resume_leadership_extracurricular_form(forms.ModelForm):
#     activity_name = forms.CharField(label='activity_name',max_length=255,required=False)
#     description = forms.CharField(label='description',widget=forms.Textarea,required=False)
    
#     class Meta:
#         model = Resume_leadership_extracurricular
#         fields = ['activity_name','description']
        
#     def clean(self):
#         cleaned_data = super().clean()
#         return cleaned_data
        
class Resume_certifications_form(forms.ModelForm):
    certification_name = SimpleArrayField(
            forms.CharField(max_length=255),
            required=False,
            delimiter=',',
            help_text="Enter certifications separated by commas"
        )    
    class Meta:
        model = Resume_certifications
        fields = ['certification_name']
        
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    
class dummy_form(forms.Form):
    name  = forms.CharField(label='input_name')
    