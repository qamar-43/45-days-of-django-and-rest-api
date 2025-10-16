from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.
#creating 2functions to display in application views 

#1. product_list
def product_list(request):
    data = ['Laltop', 'Mouse', 'Keyboard']
    dict = {'data':data}

    return JsonResponse(dict)

#creating another functin for product details
def product_details(request,product_id):
    details = f"""
        <h1 style='color=crimson'> product details for product ID: {product_id}</h1>"""
    return HttpResponse(details)