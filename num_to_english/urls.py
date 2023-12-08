from django.urls import path
from .views import default_view, num_to_english

urlpatterns = [
    path('', default_view, name='hi_dev'),
    path('num_to_english/', num_to_english, name='num_to_english'),
]
