from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse 
from .models import Arrival_details,Contact
from.forms import Contactform
import logging

# Create your views here.

def index(request):
    blog_title = "Welcome to my blog"
    
    # static demo data
    
    # posts = [{'title':'Iphone 11','description':'Description of Iphone 11'},
    #          {'title':'Iphone 12','description':'Description of Iphone 12'},
    #          {'title':'Iphone 13','description':'Description of Iphone 13'},
    #          {'title':'Iphone 14','description':'Description of Iphone 14'},
    #          {'title':'Iphone 15','description':'Description of Iphone 15'},
    #            ]
    
    
    posts = Arrival_details.objects.all() #--> for getting the inputs from the db
    return render(request,"blog/index.html",{'blog':blog_title , 'posts':posts})

def contact(request):
    
    # for get the data from the contact form in contact page.
    if request.method == 'POST':
        
        # form = Contactform(request.POST)
        
        # For getting the inputs from the form
        
            # if form.is_valid():  #---> for validating the form it is true or not
            #     logger.debug(
            #         f"Post Data is {form.cleaned_data['name']}, "
            #         f"{form.cleaned_data['email']}, "
            #         f"{form.cleaned_data['Message']}"
            #     )
                
            # print(form.cleaned_data['name']) ----> correct method for printing the values
        name = request.POST.get('name')
        email = request.POST.get('email')
        Message = request.POST.get('Message')
        
        logger = logging.getLogger("test")
        logger.debug(f'Name : {name}\nE-mail : {email}\nMessage : {Message}')
        
        
        # print(name,email,Message)  ---> correct method for printing the values
        # if name and email and Message:
        Contact.objects.create(name=name,email=email,Message=Message)
        return redirect(reverse('blog:success'))
        # else:
        # logger.debug("Form vaidation failure")
            
    return render(request,"blog/contact.html")

def collection(request):
    return render(request,"blog/collection.html")

def details(request):
    return HttpResponse("details page")

def success(request):
    return render(request,'blog/success.html')

def display(request,inp):
    return HttpResponse(f"My Name is {inp}!")

def old_url(request):
    return redirect(reverse("blog:new_page_url"))

def new_url(request):
    return HttpResponse("This is the new URL Page!")