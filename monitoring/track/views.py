from django.views.generic import TemplateView , ListView ,DetailView 
from track.models import User_track
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse 
import os
import re, uuid 
import socket 
from django.contrib.auth.models import User
import time
import pyautogui 
from django_filters.views import FilterView
# Create your views here.
# def Home(request):
#     all_list= User_track.objects.all

#     return render(request,'track/index.html' ,{'all_item':all_list})
    
# def track(request):
#     print("submitted")    
#     return render(request,'track/index.html')

    
class track(TemplateView):  
    model= User_track
    template_name = 'track/index.html'
 
    def post(self,request):
        pass



        
    def get(self,request):
        def screenshot():
            hostname = socket.gethostname()   
            ip_address = socket.gethostbyname(hostname) 
            mac_address =str(':'.join(re.findall('..', '%012x' % uuid.getnode()))) 
            user_name = User.objects.get(id=request.user.id)
            body = "nao"
            datetime = timezone.now()
            name = int(round(time.time()*1000))
            name='./images/images{}.png'.format(name)    
            time.sleep(5)
            img = pyautogui.screenshot(name)
            image = os.path.basename(name)
            print (image)
            add_user=User_track(ip_address=ip_address,mac_address=mac_address,user_name=user_name,image=image, datetime=datetime)
            add_user.save()
            print("done")
        
        starttime = time.time()
        while True:
            screenshot()
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        
        return HttpResponse("Bye")
    
class track_view(ListView):  
    model= User_track
    template_name = 'track/index.html'
    def get_queryset(self):
        return User_track.objects.filter(user_name=self.request.user)


class HomePageView(TemplateView): # new 
    model = User_track
    template_name = 'track/index.html'
    fields = ['ip_address', 'mac_address', 'body','datetime' ,'user_name']

