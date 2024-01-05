from django.shortcuts import render, get_object_or_404
from .models import Contact, Service, ContactType



def index(request):
    contacts = Contact.objects.all()
    services = Service.objects.all()
    context = {
        "contacts": contacts,
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