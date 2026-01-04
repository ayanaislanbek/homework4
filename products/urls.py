from django.urls import path
from . import views


urlpatterns = [
    path('product_one/', views.product_one),
    path('product_two/', views.product_two),
    path('product_three/', views.product_three),

]
#     path('products/', views.product),
#     path('products/<int:id>/', views.product_detail), 
# ]
