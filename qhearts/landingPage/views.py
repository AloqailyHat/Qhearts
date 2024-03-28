# landingPage/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def adopt(request):
    return render(request, 'adopt.html')

def rescue(request):
    return render(request, 'rescue.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            return redirect('contact_success') 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
