from django.shortcuts import render, get_object_or_404



def index(request):
    return render(request, "app/base.html")


def service(request):
    return render(request,"app/service.html")