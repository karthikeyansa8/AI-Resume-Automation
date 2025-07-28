from django import forms
from django.contrib.auth.models import User

class Contactform(forms.Form):
    
    name = forms.CharField(label='name',max_length=30 )
    email = forms.EmailField(label='email')
    Message = forms.CharField(label='Message')
    
    
    
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username',max_length=30)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password',max_length=10)
    confirm_password = forms.CharField(label='password',max_length=10)
    
    class Meta:    #---> for insert the details in the auth user table 
        model = User
        fields = ['username',
                  'email',
                  'password']
        