from django.urls import path
from .views import generate_barcode


urlpatterns = [
        path('', generate_barcode, name='barcode'),
        ]
