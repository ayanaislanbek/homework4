from django.urls import path 
from .import views 

urlpatterns =[
    path('clothes_list/', views.clothes_list, name='clothes'),
    path('clothes/dolce-gabbana/', views.first_brand, name='first_brand'),
    path('clothes/alexander-mcqueen/', views.second_brand, name='second_brand'),
]