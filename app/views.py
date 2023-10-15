from django.shortcuts import render, get_object_or_404



def index(request):
    return render(request, "app/main.html")


def service(request):
    return render(request,"app/service.html")

def contact(request):
    return render(request,"app/contact.html")