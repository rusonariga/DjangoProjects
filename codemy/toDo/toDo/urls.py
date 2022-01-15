from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from toDo_list import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toDo_list.urls')),
]
