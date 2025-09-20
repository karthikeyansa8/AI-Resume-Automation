from django.shortcuts import render,redirect
from django.http import HttpResponse
from boomers.Resume_generation import create_resume
from boomers.models import Person_Details, Resume_Education, Resume_Internships, Resume_Projects, Resume_Skills, Resume_certifications, resume_personal_details
from boomers.forms import Resume_Education_form, Loginform, RegistrationForm, Reset_password_form, Resume_Internships_form, Resume_Projects_form, Resume_Skills_form, Resume_certifications_form, Resume_personal_details_form, dummy_form, forgot_password_form
from django.contrib.auth.models import User
from django.contrib import messages # ---> for send a success message
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout #--> for authentication
from django.urls import path,reverse 
from django.contrib.auth.tokens import default_token_generator  # --> for token generator
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode# --> for generate a 
from django.utils.encoding import force_bytes # --> for encode a string
from django.contrib.sites.shortcuts import get_current_site # --> for get current site
from django.template.loader import render_to_string # --> for render a template to str
from django.core.mail import send_mail # --> for send a mail
from django.contrib.auth.decorators import login_required # --> for login required decorator
from django.forms import formset_factory
import os
from django.http import FileResponse, Http404
from django.conf import settings
# Create your views here.

@login_required(login_url='/login') # --> for login required decorator
def index(request):
    
    # print('request: ',request.user) # ---> output eg: karthi39
    person_details = Person_Details.objects.all()
    
    
    # for person in person_details:
    #     print(person)
        
      # output:
    """Person_Details object (1)
            Person_Details object (2)
            Person_Details object (3)
            Person_Details object (4)
            Person_Details object (5)
            Person_Details object (6)
            Person_Details object (7)
            Person_Details object (8)
            Person_Details object (9)"""
    
    # person_details = Person_Details.objects.filter(auth_id = request.user) # ---> the auth_id is feild in the models file
    # person_details = Person_Details.objects.filter(auth_id_id = request.user.id) # ---> the auth_id_id is the DB column name
    return render(request,"boomers/index.html",{'person_details':person_details})

def detail(request,slug):
    """_summary_

    Args:
        request (_type_): _description_
        slug (str): inp for getting single row 

    Returns:
        _type_: _description_
    """
    
    # print(request,request.user)
    
    person_detail = Person_Details.objects.get(slug=slug) #--> For get the details with the slug field
    
    # print(person_details.role,person_details.name) #---> output : Backend Developer Karthick L C
    
    # print(person_detail)  #---> output:Karthick L C
        
    return render(request,'boomers/detail.html',{'person_detail':person_detail})

def register(request):
    # print(request)
    # print('user',request.user) # ---> for check user is logged out Output eg:  AnonymousUser  if logged in gives the username 
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            passw = form.save(commit=False)
            passw.set_password(form.cleaned_data['password']) # --> for hashing the password
            passw.save()
            print("Register Success!")
            messages.success(request,'Registered Successfully! Now you can login')
            return redirect(reverse('login'))
            
        
        # username  = request.POST.get('username')
        # email  = request.POST.get('email')
        # password  = request.POST.get('password')
        
        # try:
        #     if username and email and password:
        #         User.objects.create_user(username=username, email=email, password=password)  # ---> insert the values to the auth user table 
        #         print('Successfully Inserted!')
        # except Exception as e:
        #     print("error",{e})
        
    return render(request,'boomers/register.html',{'form':form})

def login(request):
    
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username,password=password)
            # print("user:",user) #--> gives the username eg:karthi39
            
            if user is not None:
                auth_login(request,user)
                print('Successfully Login!')
                # messages.success(request,'Login Successfully!')
                return redirect(reverse('index'))
                
    return render(request,'boomers/login.html',{'form':form})

def logout(request):
    auth_logout(request) # --> for logout 
    return redirect(reverse('register'))
    
    
def forgot_password(request):
    
    form = forgot_password_form()
    
    if request.method == 'POST':
        
        form = forgot_password_form(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            user  = User.objects.get(email=email)
            # print('views',user.pk)  #--->eg: user.pk = 1 , user = karthi39
            
            # send email for reset password
            
            # create a url with token, uid and domain name
            token = default_token_generator.make_token(user) # --> create a token for user to reset password (one time use)
            uid = urlsafe_base64_encode(force_bytes(user.pk)) # --> encode the user id to base64 gives eg: b'cGFzc3dvcmQx' in short gives the base64 str
            current_site =  get_current_site(request) 
            domain = current_site.domain #--> get the domain name eg: 127.0.0.1:8000
            
            #mail summary :
            subject = "Reset Password Requested"
            message  = render_to_string('boomers/reset_password_email.html',{
                'domain':domain,
                'uid':uid,
                'token':token
            }) 
            
            send_mail(subject,message,from_email='noreplay@honest.com',recipient_list=[email])
            messages.success(request,'Email has been sent!')
            
            # return redirect(reverse('reset_password_email'))
            
            
    return render(request,'boomers/forgot_password.html',{'form':form})



def reset_password_email(request,uidb64,token):
    form = Reset_password_form()
    if request.method == 'POST':
        
        form = Reset_password_form(request.POST)
        
        if form.is_valid():
            password = form.cleaned_data['new_password']
            
            try:
                uid = urlsafe_base64_decode(uidb64)
                user = User.objects.get(id=uid)
            except Exception as e:
                user = None
            
            if user is not None and default_token_generator.check_token(user,token):
                user.set_password(password)
                user.save()
                messages.success(request,'your password has been reset')
                return redirect(reverse('login'))
            else:
                messages.error(request,'Password reset link Invalid')
            
    return render(request,'boomers/reset_password.html',{'form':form})
    
    
# @login_required(login_url='login') # --> for login required decorator
def resume_form(request):
    
    # personal_details
    personal_details_form  = Resume_personal_details_form()
    
    # education  
    education_form = Resume_Education_form()
    
    # skills      
    skills_form = Resume_Skills_form()
    
    #Projects
    projects_form = Resume_Projects_form()
    
    # internships
    internships_form = Resume_Internships_form()
    
    #extracuriculars
    # extracurilcular_form = Resume_leadership_extracurricular_form()
    
    # certifications
    certifications_form = Resume_certifications_form()
    
    if request.method == 'POST':
        # personal details
        personal_details_form = Resume_personal_details_form(request.POST,request.FILES)
        
        # education
        education_form = Resume_Education_form(request.POST)
        
        # skills
        skills_form = Resume_Skills_form(request.POST)
        
        # Projects
        try:
            count = int(request.POST.get('project_count'))
        except (ValueError, TypeError):
            count = 0
            
        projects_form = Resume_Projects_form(request.POST,project_count=count)  
            
        # Internships
        internships_form = Resume_Internships_form(request.POST)
        
        # Extracurriculars
        # extracurilcular_form = Resume_leadership_extracurricular_form(request.POST)
        
        # Certifications
        certifications_form = Resume_certifications_form(request.POST)
        
        
        
        if (personal_details_form.is_valid() and  education_form.is_valid() and 
            skills_form.is_valid() and projects_form.is_valid() and internships_form.is_valid() and 
            """extracurilcular_form.is_valid()""" and certifications_form.is_valid() ):
            
            #personal details
            personal_details_form.save()
            
            
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            try:
                user = resume_personal_details.objects.get(email=email,first_name=first_name,last_name=last_name)  # --> get the user from the DB
                request.session["user_id"] = user.id  # --> store the user id in the session
    
            except :
                request.session.pop("user_id", None) # --> if user not found set the session user_id to None
                user = None

            #education
            edu = education_form.save(commit=False)  # --> to save the form without committing to the DB
            if user is not  None:
                edu.person_id_id = user.id
                edu.save()
            
            
            #skills
            skill = skills_form.save(commit=False)
            if user is not None:
                skill.person_id_id = user.id
                skill.save()
            
            #projects
            for i in range(1,count+1):
                if request.POST.get(f'project{i}_name') and request.POST.get(f'project{i}_keywords') and request.POST.get(f'project{i}_description'):
                    project = projects_form.save(commit=False)
                    if user is not None:
                        project.person_id_id = user.id
                        project.save()
            
            #internships
            internship_fields = ['company_name', 'role', 'location', 'duration', 'start_date', 'end_date']
            for field in internship_fields:
                if request.POST.get(field): 
                    if internships_form.is_valid():
                        intern = internships_form.save(commit=False)
                        if user is not None:
                            intern.person_id_id = user.id
                            intern.save()
    
            # #extracurilculars
            # leadership_extracurricular = ['activity_name', 'description']
            # for field in leadership_extracurricular:
            #     if request.POST.get(field): 
            #         if extracurilcular_form.is_valid():
            #             extra = extracurilcular_form.save(commit=False)
            #             if user is not None:
            #                 extra.person_id_id = user.id
            #                 extra.save()
                
        
            # certifications
            certifications = ['certification_name']
            for field in certifications:
                if request.POST.get(field): 
                    if certifications_form.is_valid():
                        cer = certifications_form.save(commit=False)
                        if user is not None:
                            cer.person_id_id = user.id
                            cer.save()

            messages.success(request,'Details are valid!')
            # return user.id
                        
            
        else:
            print("Form is invalid")
            messages.error(request,'Details is invalid, please check the All the Section fields')
   
   
    return render(request,'boomers/resume_form.html',{'personal_details_form':personal_details_form,
                                                      'education_form':education_form,
                                                      'skills_form':skills_form,
                                                      'projects_form':projects_form,
                                                      'internships_form':internships_form,
                                                    #   'extracurilcular_form':extracurilcular_form,
                                                      'certifications_form':certifications_form})
    
# ------>   dummy  
def dummy(request):
    
    # formset = dummy_form()
    # if request.method == 'POST':
    #     formser = dummy_form(request.POST)
        
    dummy_formset = formset_factory(dummy_form, extra=3)  # --> create a formset with 2 extra forms
    if request.method == 'POST':
        formset = dummy_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data['name'])  # --> print the changed data in the form
    return render(request,'boomers/dummy.html',{'forms':dummy_formset})


# class ResumeGeneration:
def generateresume(request):
    
    user_id = request.session.get("user_id")  # --> get the user id from the session
    print("user_id-->",user_id)
    if user_id is not None:
        try:
            try:
                personal_detail = resume_personal_details.objects.get(id=user_id)  # --> get the user details from the DB
            except :
                personal_detail = None
            try:
                education_detail = Resume_Education.objects.get(person_id_id=user_id)  # --> get the education details from the DB
            except:
                education_detail = None
            try:
                skills_detail = Resume_Skills.objects.get(person_id_id=user_id)  # --> get the skills details from the DB
            except:
                skills_detail = None
            try:
                projects_detail = Resume_Projects.objects.get(person_id_id=user_id)  # --> get the projects details from the DB
            except:
                projects_detail = None
            try:
                internships_detail = Resume_Internships.objects.get(person_id_id=user_id)  # --> get the internships details from the DB
            except:
                internships_detail = None
            # try:
            #     extracurricular_detail = Resume_leadership_extracurricular.objects.get(person_id_id=user_id)  # --> get the extracurricular details from the DB
            # except:
            #     extracurricular_detail = None
            try:
                certifications_detail = Resume_certifications.objects.get(person_id_id=user_id)  # --> get the certifications details from the DB
            except:
                certifications_detail = None
                            
            print('personal_detail:',personal_detail,'\neducation_detail:',education_detail,'\nskills_detail:',skills_detail,
                '\nprojects_detail:',projects_detail,'\ninternships_detail:',internships_detail,
                # '\nextracurricular_detail:',extracurricular_detail,
                '\ncertifications_detail:',certifications_detail)

        except Exception as e:
            # print("Error occurred:", e)
            raise Exception("Failed to fetch user details")
        
        #-----------> Resume generation call part <---------------

        resume_generation = create_resume(personal_detail,education_detail,skills_detail,
                                            projects_detail,internships_detail,
                                        #   extracurricular_detail,
                                            certifications_detail)
        resume_generation.main()  # --> call the resume method to create a resume
        
        #-----------> Resume generation call part <---------------
        
        # Return the resume file 
        filename = f"{personal_detail.first_name}_{personal_detail.last_name}_Resume.docx"
        resume_folder = os.path.join(settings.BASE_DIR, "Resumes")
        file_path = os.path.join(resume_folder, filename)

        if not os.path.exists(file_path):
            raise Http404("Resume not found")

        response = FileResponse(
            open(file_path, "rb"),
            content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    
    else:
        raise Http404("User details not found ")
    
    # return render(request,"boomers/generateresume.html")
    # return HttpResponse('Resume Created Successfully')

def download_resume(request):
    user_id = request.session.get("user_id")
    if not user_id:
        raise Http404("User not found in session")

    try:
        personal_detail = resume_personal_details.objects.get(id=user_id)
    except resume_personal_details.DoesNotExist:
        raise Http404("Personal details not found")

    filename = f"{personal_detail.first_name}_{personal_detail.last_name}_Resume.docx"
    resume_folder = os.path.join(settings.BASE_DIR, "Resumes")
    file_path = os.path.join(resume_folder, filename)

    if not os.path.exists(file_path):
        raise Http404("Resume not found")

    response = FileResponse(
        open(file_path, "rb"),
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
