from django.shortcuts import render,redirect
from django.http import HttpResponse
from boomers.models import Person_Details, Resume_Education, resume_personal_details
from boomers.forms import Education_form, Loginform, RegistrationForm, Reset_password_form, Resume_personal_details_form, forgot_password_form
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
    
    
@login_required(login_url='login') # --> for login required decorator
def resume_form(request):
    form  = Resume_personal_details_form()
    if request.method == 'POST':
        form = Resume_personal_details_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'boomers/resume_form.html',{'form':form})