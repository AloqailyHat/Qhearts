# landingPage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),  # URL pattern for landing page
    path('about/', views.about, name='about'),
    path('adopt/', views.adopt, name='adopt'),
    path('rescue/', views.rescue, name='rescue'),  
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
