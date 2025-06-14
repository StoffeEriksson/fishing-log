from django.urls import path
from .views import home, dashboard, log_fish_session, session_list, session_stats, reset_stats, delete_account

urlpatterns = [
    path('', home, name='home'),
    path('log/', log_fish_session, name='log_fish'),
    path('dashboard/', dashboard, name='dashboard'),
    path('sessions/', session_list, name='session_list'),
    path('stats/', session_stats, name='session_stats'),
    path('reset/', reset_stats, name='reset_stats'),
    path('accounts/delete/', delete_account, name='account_delete'),
    
]