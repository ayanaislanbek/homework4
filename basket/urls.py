from django.urls import path
from basket import views

urlpatterns = [
    path('basket/', views.show_basket_view, name='show_basket'),        
    path('basket_list/', views.create_basket_view, name='create_basket'),
    path('basket_list/<int:id>/edit', views.edit_user_view, name='edit_user'), 
    path('basket_list/<int:id>/delete', views.delete_basket_view, name='delete_basket'),
]
