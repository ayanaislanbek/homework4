from django.urls import path 
from .import views 

urlpatterns = [
    path('sign_up/', views.AccountCreationView.as_view(),name='sign_up'),
    path('sign_in/', views.AuthSessionView.as_view(),name='sign_in'),
    path('developer_list/', views.DeveloperListView.as_view(),name='developer_list'),
    path('sign_out/', views.SignOutView.as_view(), name='sign_out'),
]