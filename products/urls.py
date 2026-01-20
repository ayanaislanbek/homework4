from django.urls import path
from . import views


urlpatterns = [
    path('product_one/', views.korean_food, name='product_one'),
    path('product_two/', views.current_time),
    path('product_three/', views.about_me, name='product_three'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('products_list/', views.ProductsView.as_view(), name='home_page') , 
    path('product_list/<int:id>/',views.ProductsDetailView.as_view(),name='product_detail'),
]
