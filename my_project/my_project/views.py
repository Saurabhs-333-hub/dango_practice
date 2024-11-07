from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # return HttpResponse("Hello World!, I am Home!")
    return render(request, "home.html")


def about_page(request):
    # return HttpResponse("About Page")
    return render(request, "about.html")
