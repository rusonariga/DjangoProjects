from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('delete/<list_id>', views.item_delete, name="delete"),
    path('status/<list_id>', views.item_change_status, name="change_status"),
]
