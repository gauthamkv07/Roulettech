from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_user, name = 'create_user'),
    path('users/all/', views.get_users, name='get_users'),
]