# myproject/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('sixthSense.urls')),  # Include sixthSense app URLs
]