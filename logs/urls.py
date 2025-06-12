from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    path('log/', views.log_fish_session, name='log_fish'),
]