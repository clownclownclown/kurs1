from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', show_main_page, name='main_page'),
    path('history/', show_history_page, name='history'),
    path('delete_history/', delete_history, name='delete_history')
]