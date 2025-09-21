from  django.core.management.base import BaseCommand 

from boomers.models import resume_personal_details


class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        
        
        
        user = resume_personal_details.objects.filter(email='karthikeyansa8@gmail.com',first_name='Karthikeyan',last_name='S A').last()  # --> get the user from the DB
        print(user.id)