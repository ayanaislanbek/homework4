from django.urls import path 
from .import views 

urlpatterns = [
    path('sign_up/', views.account_creation_view,name='sign_up'),
    path('sign_in/', views.auth_session_view,name='sign_in'),
    path('developer_list/', views.developer_list_view,name='developer_list'),
    path('sign_out/', views.sign_out_view, name='sign_out'),
]