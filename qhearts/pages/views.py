# pages/views.py
from django.shortcuts import render

def index(request):
    # You can add any context data you need here
    return render(request, 'landing.html')