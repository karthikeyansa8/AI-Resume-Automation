from django.urls import reverse
from django.shortcuts import redirect
import re

class RegisteredUserMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        if request.user.is_authenticated: # if user is logged in
            
            path_restrict = [reverse('register'),reverse('login')]
            
            if request.path in path_restrict:
                return redirect(reverse('index'))
        
        # response = self.get_response(request)
        
        return self.get_response(request)
    
class RestrictUnregisterMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        if not request.user.is_authenticated: # --> it means user is not logged in
            # path_restrict = [reverse('index'),
            #                   r'^/detail/.+'  # match any slug
            #                  ] 
            
            path = request.path  # for example: /detail/123
            # print(path)
   
            if path == reverse('index') :
                return redirect(reverse('register'))
            
            
            if re.match(r'^/boomers/detail/.+', path):
                return redirect(reverse('register'))
            
        # response = self.get_response(request)
        
        return self.get_response(request)
        
    
        
        