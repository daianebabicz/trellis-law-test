from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('num_to_english.urls')),
    path('', include('num_to_english.urls')), 
]
