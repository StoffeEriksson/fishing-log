from django.urls import path
from .views import home, dashboard, log_fish_session

urlpatterns = [
    path('', home, name='home'),
    path('log/', log_fish_session, name='log_fish'),
    path('dashboard/', dashboard, name='dashboard'),
    
]