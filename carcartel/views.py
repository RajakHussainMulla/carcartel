from django.shortcuts import redirect, render

from carcartel.models import Team
from cars.models import Car

from django.contrib import messages

from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True)
    teams=Team.objects.all()
    all_cars=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'carcartel/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams
    }
    return render(request,'carcartel/about.html',data)

def services(request):
    return render(request,'carcartel/services.html')

def contact(request):
    if request.method=='POST':
         name=request.POST['name']
         email=request.POST['email']
         subject=request.POST['subject']
         phone=request.POST['message']
         message=request.POST['message']
          
         email_subject='you have a new message from CarZone website regarding ' + subject
         message_body='Name:' + name + '. Email:  ' + email + '. Phone: ' + phone + '. message: ' + message
    
         admin_info=User.objects.get(is_superuser=True)
         admin_email=admin_info.email
         send_mail(
               email_subject,
               message_body,
               'mullarajak123@gmail.com',
               [admin_email],
               fail_silently=False,
            ) 
         messages.success(request, 'Thank you for contacting us. we will get back to you shortly')  
         return redirect('contact')
    return render(request,'carcartel/contact.html')