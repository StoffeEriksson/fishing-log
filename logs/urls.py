from django.urls import path
from .views import home_or_dashboard, dashboard, log_fish_session

urlpatterns = [
    path('', home_or_dashboard, name='home'),
    path('log/', log_fish_session, name='log_fish'),
    path('dashboard/', dashboard, name='dashboard'),
    
]