from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:id>', views.products_category, name='products_category'),
]
