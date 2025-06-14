from django.urls import path
from .views import delete_account

urlpatterns = [
    path('delete/', delete_account, name='account_delete'),
]