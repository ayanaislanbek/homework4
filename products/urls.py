from django.urls import path
from . import views


urlpatterns = [
    path('product_one/', views.korean_food),
    path('product_two/', views.current_time),
    path('product_three/', views.about_me),
    path('products_list/', views.products), 
    path('products_list/<int:id>', views.product_detail),
    
]
