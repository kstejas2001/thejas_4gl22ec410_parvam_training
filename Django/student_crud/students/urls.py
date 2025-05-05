from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #HOME Page
    path('about/', views.about_us, name='about'), #About Us Page
    path('service/', views.service, name='service'), #Service Page
    path('contact/', views.contact, name='contact'), #Contact Us Page
]