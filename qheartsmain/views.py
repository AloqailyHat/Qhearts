from django.shortcuts import render, redirect
from .forms import RescueReportForm, ContactForm
from .models import RescueReport

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def adopt(request):
    return render(request, 'adopt.html')

def report(request):
    if request.method == 'POST':
        form = RescueReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RescueReportForm()
    return render(request, 'report.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., save it to the database, send an email, etc.)
            return redirect('contact_form_page')  # Redirect after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def report_rescue_page(request):
    if request.method == 'POST':
        form = RescueReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RescueReportForm()
    return render(request, 'report_form.html', {'form': form})

def report_list(request):
    reports = RescueReport.objects.all()
    return render(request, 'report_list.html', {'reports': reports})
