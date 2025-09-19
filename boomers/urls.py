from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<str:slug>', views.detail, name='detail'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logut/', views.logout,name='logout'),
    path('forgotpassword/', views.forgot_password,name='forgot_password'),
    path('resetpassword/<uidb64>/<token>', views.reset_password_email,name='reset_password_email'),
    path('resumeform/', views.resume_form,name='resumeform'),
    path('dummy/',views.dummy,name='dummy'),
    path('generateresume/',views.generateresume,name='generateresume'),
    path('download-resume/', views.download_resume, name='download_resume'),
    
]
