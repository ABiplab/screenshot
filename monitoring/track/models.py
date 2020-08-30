from django.db import models

# Create your models here.
class User_track(models.Model): 
    ip_address = models.CharField(max_length=200) 
    mac_address = models.CharField(max_length=200) 
    user_name = models.ForeignKey( 'auth.User', on_delete=models.CASCADE, ) 
    image  = models.ImageField(upload_to='images')
    datetime = models.DateTimeField() 
