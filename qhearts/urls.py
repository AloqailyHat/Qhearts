from django.contrib import admin
from django.urls import path
from qheartsmain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('adopt/', views.adopt, name='adopt'),
    path('report/', views.report_rescue_page, name='report_rescue_page'),
    path('report/submit/', views.report, name='report_rescue'),
    path('contact/', views.contact, name='contact'),
    path('contact/form/', views.contact_form, name='contact_form_page'),
    path('reports/', views.report_list, name='report_list'), 
]
