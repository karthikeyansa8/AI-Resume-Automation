from blog.models import Arrival_details # ---> import the model content 
from  django.core.management.base import BaseCommand #--> import maually for extend the class basecommand


class Command(BaseCommand):  #--> Must give the class name as Command "C is capital letter"
    
    help = "This command is for inserting new_arrival data to DB"

    def handle(self, *args, **options):
        
        # Arrival_details.objects.all().delete()  ---> this line is for deleting the row in the DB
        
        titles = [
            'IPHONE 11',
            'IPHONE 12',
            'IPHONE 12 Mini',
            'IPHONE 13',
            'IPHONE 13 Pro Max',
            'IPHONE 14',
            'IPHONE 14 Pro Max',
            'IPHONE 15',
            'IPHONE 15 Pro Max',
            'IPHONE 16 Pro Max',
        ]

        descriptions = [
            'The iPhone 11 is a smartphone developed by Apple Inc.',
            'The iPhone 12 is a smartphone developed by Apple Inc.',
            'The iPhone 12 Mini is a smartphone developed by Apple Inc.',
            'The iPhone 13 is a smartphone developed by Apple Inc.',
            'The iPhone 13 Pro Max is a smartphone developed by Apple Inc.',
            'The iPhone 14 is a smartphone developed by Apple Inc.',
            'The iPhone 14 Pro Max is a smartphone developed by Apple Inc.',
            'The iPhone 15 is a smartphone developed by Apple Inc.',
            'The iPhone 15 Pro Max is a smartphone developed by Apple Inc.',
            'The iPhone 16 Pro Max is a smartphone developed by Apple Inc.',
        ]

        img_urls = [
            'blog/img/iphone 11.jpg',
            'blog/img/iphone-12.webp',
            'blog/img/iphone-12-mini.webp',
            'blog/img/iphone13.jpg',
            'blog/img/iphone 13 pro.webp',
            'blog/img/iphone-14.webp',
            'blog/img/iphone-14-pro-.jpeg',
            'blog/img/iphone 15 promax.webp',
            'blog/img/iphone 15 promax.webp',
            'blog/img/iphone 15 promax.webp',
        ]

        for title, description, img_url in zip(titles, descriptions, img_urls):
            """ Inside the create function give the correct variable name 
            for eg: in the model file the variable name is title, description, img_url
            so here we are giving the same name to the variables title , description, img_url
            """
            Arrival_details.objects.create(new_arrival_title=title, new_arrival_description=description, new_arrival_img_url=img_url) # ---> create a new object in the model content

        self.stdout.write(self.style.SUCCESS("Completed inserting data to DB"))  #--> For konwing the data is successfully inserted in the db printed in the terminal