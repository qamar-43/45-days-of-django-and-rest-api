from django.urls import path
from customer import views


#order application urls which we need to connect with onlinestore configyration
urlpatterns = [
    path('profile/', views.profile),
    path('dashboard/', views.dashboard),
]
