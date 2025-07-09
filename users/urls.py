# users/urls.py
from django.urls import path
from .views import team_list_view, add_user_view

app_name = 'users'

urlpatterns = [
    path('', team_list_view, name='team_list'),
    path('add/', add_user_view, name='add_user'),
]