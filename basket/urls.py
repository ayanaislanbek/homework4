from django.urls import path
from basket import views

urlpatterns = [
    path('basket/', views.ShowBasketView.as_view(), name='show_basket'),        
    path('basket_list/', views.CreateBasketView.as_view(), name='create_basket'),
    path('basket_list/<int:id>/edit', views.EditUserView.as_view(), name='edit_user'), 
    path('basket_list/<int:id>/delete', views.DeleteBasketView.as_view(), name='delete_basket'),
]
