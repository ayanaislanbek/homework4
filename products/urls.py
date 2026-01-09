from django.urls import path
from . import views


urlpatterns = [
    path('product_one/', views.korean_food, name='product_one'),
    path('product_two/', views.current_time),
    path('product_three/', views.about_me, name='product_three'),

    path('products_list/', views.products, name='home_page') , 
    path('product_list/<int:id>/', views.product_detail),
]
