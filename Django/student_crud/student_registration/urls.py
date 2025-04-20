from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_list, name='list'),              
    path('create/', views.registration_form, name='form'),               
    path('<int:pk>/', views.view_registration, name='view'),               
    path('<int:pk>/edit/', views.update_registration, name='update'),               
    path('<int:pk>/delete/', views.delete_registration, name='delete'),               
]