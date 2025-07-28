from django.urls import path
from . import views

# --> must give (urlpatterns) 

app_name = 'blog'

urlpatterns =[

    path("index/",views.index,name="index"),
    # path("index/contact/",views.contact,name="contact"),
    # path("index/collection/",views.collection,name="collection"),
    path('details/',views.details,name="details"),
    path('display/<str:inp>/',views.display,name="display"),
    path('old_url/',views.old_url,name="old_url"),
    path('new_anything_url/',views.new_url,name="new_page_url"),
    path('contact/',views.contact,name='contact'),
    path('collection/',views.collection,name='collection'),
    path('success/',views.success,name='success'),
]