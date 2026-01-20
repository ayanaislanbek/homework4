from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:id>', views.ProductCategoriesListView.as_view(), name='products_category'),
]
