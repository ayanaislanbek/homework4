from django.urls import path
from .import views

urlpatterns = [
    path('registration/', views.signup_view, name='registration'),
    path('logon/', views.logon_view, name='logon'),
    path('add_movie', views.add_movie_view, name='add_movie'),
    path('movie_list', views.show_movie_view, name='movie_list'),
    path('movie_list/<int:id>/update', views.edit_movie_view, name='edit_movie'),
    path('movie_list/<int:id>/delete', views.delete_movie_view, name='delete_movie'),
    path('search/', views.search_view, name='search')
]
