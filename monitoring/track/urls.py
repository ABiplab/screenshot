from django.urls import path
from .views import HomePageView ,track ,track_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
     path('track_view/', track_view.as_view(), name='track_view'), 
      path('track/', track.as_view(), name='track'),  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)