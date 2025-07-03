# users/urls.py
from django.urls import path
from .views import team_list_view

app_name = 'users'

urlpatterns = [
    path('', team_list_view, name='team_list'),
]