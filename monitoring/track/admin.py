from django.contrib import admin

# Register your models here.
from .models import User_track

class User_trackfilter(admin.ModelAdmin):
    list_display = ('user_name', 'datetime', 'ip_address','mac_address')
    list_filter = ( 'datetime',)
    search_fields = ('user_name','datetime',)

admin.site.register(User_track,User_trackfilter)