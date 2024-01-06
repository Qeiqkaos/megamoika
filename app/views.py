from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from .models import Contact, Service, ContactType
import json



def index(request):
    contacts = Contact.objects.all()
    services = Service.objects.all()
    
    # Serialize Service objects to JSON
    services_json = serialize('json', services)

    context = {
        "contacts": contacts,
        "services": services,
        "services_json": json.dumps(services_json),
        "contactType": ContactType,
    }
    return render(request, "app/main.html", context)


def services_view(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request,"app/service.html", context)