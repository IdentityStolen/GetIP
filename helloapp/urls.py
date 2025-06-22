from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_name_and_show_ip, name='ask_name_and_show_ip'),
]

