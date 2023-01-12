from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.base, name='base'),
    path("about/", views.about, name='about'),
    path("home/", views.home, name='home'),
    path("services/", views.services, name='services'),
    path("contacts/", views.contacts, name='contacts')
    ]