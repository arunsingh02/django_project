from django.shortcuts import render, HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages


def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'index.html')

def home(request):
    # return HttpResponse("This is the Home page.")
    # context={
    #     'addr': 'Hisar, Haryana',
    #     'profession': 'Business'
    # }
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date_time=datetime.today())
        contact.save()
        messages.success(request, "We appreciate you reaching out to us. We will respond as soon as possible.")
    return render(request, 'contacts.html')
    
