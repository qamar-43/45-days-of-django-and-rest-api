from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
#1. creating place_order function to place order
def place_order(request):
    return HttpResponse ('<h1>Order placed succesfully</h1>')



#2. creating another function order_history to check order history
def order_history(request):

#creating  2lists in a dictionary 
    orders = [ 
    {'id':1, 'item':'laptop', 'status':'delivered'},
    {'id':2, 'item':'earbuds', 'status':'shipped'},
]
    dict = {'orders':orders}
    return JsonResponse(dict)