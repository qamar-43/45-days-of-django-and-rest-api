from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view, name='home'),
    path('news/<str:category>/', views.news_view, name='news'),
]
