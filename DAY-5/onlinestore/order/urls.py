from django.urls import path
from order import views


#order application urls which we need to connect with onlinestore configyration
urlpatterns = [
    path('place/', views.place_order),
    path('history/', views.order_history),
]
