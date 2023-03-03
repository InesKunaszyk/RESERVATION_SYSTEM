"""RESERVATION URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import rs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rs.views.room_list, name='start'),
    path('rooms/', rs.views.show_rooms, name='show_rooms'),
    path('add/', rs.views.add_room, name='add_room'),
    path('edit/<int:room_id>/', rs.views.edit_room, name='edit_room'),
    path('details/<int:room_id>/', rs.views.room_details, name='room_detail'),
    path('delete/<int:room_id>', rs.views.delete_room, name='delete_room'),
    path('reserve/<int:room_id>', rs.views.add_reservation, name='reserve_room'),
]
