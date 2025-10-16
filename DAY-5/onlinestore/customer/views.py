from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
#CREATING 2functions for custo mer application
#1.profile function
def profile(request):
    # key: value
    customer_profile ={
    'name': 'Doraemon',
    'email': 'dora@gmail.com',
    'membership': 'premium',
    }

    return JsonResponse(customer_profile)

#creating another function of dashboard
def dashboard(request):
    customer_dashboard = """
            <h1 style='color:violet; font-size:60px;>
            Welcome to Customer Dashboard
            </h1>


            """
    return HttpResponse(customer_dashboard)