from django.shortcuts import render, get_object_or_404
from .models import Contact, Service, ContactType



def index(request):
    services = Service.objects.all()
    context = {
        "contact": Contact,
        "services": services,
        "contactType": ContactType,
    }
    return render(request, "app/main.html", context)


def services_view(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request,"app/service.html", context)


def contact(request):
    contacts = Contact.objects.all()
    return render(request,"app/contact.html",{'contacts': contacts})