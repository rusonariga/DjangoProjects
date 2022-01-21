from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('registration/', views.user_registration, name="user_registration"),
    path('profile_edit/', views.user_profile_edit, name="user_profile_edit"),
    path('password_update/', views.user_password_update,
         name="user_password_update"),
]
