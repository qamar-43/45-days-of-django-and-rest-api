from django.urls import path
from product import views


#order application urls which we need to connect with onlinestore configyration
urlpatterns = [
    path('', views.product_list),
    path('<int:product_id>/', views.product_details),
]
