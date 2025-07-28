from  django.core.management.base import BaseCommand 

from boomers.models import Person_Details


class Command(BaseCommand):
    
    help = "To insert the person details in the DB"
    
    def handle(self, *args, **options):
        
        # Person_Details.objects.all().delete   # for deleting the exsisting data
        
        
        names =[
            'Dhayanithi K',
            'Dhayanithi V',
            'Karthick L C',
            'Karthikeyan S A',
            'Krishna K',
            'Kishore Sriram',
            'Rohith S',
            'Sachin S',
            'Sujith R',
            
        ]
        
        reg_nos = [
            7,8,22,23,26,27,40,41,51
        ]
        
        departments = [
            'AI&DS',
            'AI&DS',
            'AI&DS',
            'AI&DS',
            'AI&DS',
            'AI&DS',
            'AI&DS',
            'AI&DS',
            'AI&DS',
            
        ]
        
        roles = [
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            'Backend Developer',
            
        ]
        
        emails = [
            'nithik8@gmail.com',
            'dhayaswini@gmail.com',
            'karthicklc2@gmail.com',
            'karthikeyansa4@gmail.com',
            'kishoresriram@gmail.com',
            'krishnakk@gmail.com',
            'rohithsivasamy2@gmail.com',
            'sachinsurender3@gmail.com',
            'sujithramesh2@gmail.com',
        ]
        
        phone_numbers = [
            '1234567890',
            '1234567890',
            '1234567890',
            '1234567890',
            '1234567890',
            '1234567890',
            '1234567890',
            '1234567890',
            '1234567890',
        ]
        
        for name, reg_no, department, role, email, phone_number in zip(names, reg_nos, departments, roles, emails, phone_numbers):
            
            Person_Details.objects.create(name=name, 
                                          reg_no=reg_no, 
                                          department=department, 
                                          role=role, 
                                          email=email, 
                                          phone_number=phone_number)
            # print(Person_Details())
            
        self.stdout.write(self.style.SUCCESS("Completed Inserting the persons Data!"))
            

