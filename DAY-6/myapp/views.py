from django.shortcuts import render
from django.http import HttpResponse

def demo_view(request):
    return HttpResponse("<h1>Hello from Humera’s Django app!</h1>")


def home_view(request):
    return HttpResponse("welcome to my portfolio website. I am a web developer. Will help you Build your dream app with Django" )


def about_view(request):
    return HttpResponse("welcome to about page for more info")