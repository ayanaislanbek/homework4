from django.urls import path
from . import views


urlpatterns = [
    path('product_one/', views.korean_food),
    path('product_two/', views.current_time),
    path('product_three/', views.about_me),
    
]