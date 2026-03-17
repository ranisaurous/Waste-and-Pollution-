from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),

   path('create-report', views.createOcean, name="create-report"),
    path('read-report', views.readOceans, name="read-report"),
    path('read-report/<str:pk>', views.readOcean, name="read-report"),
    path('update-report/<str:pk>', views.updateOcean, name="update-report"),
    path('delete-report/<str:pk>', views.deleteOcean, name="delete-report"),

   path('maps/', views.maps, name='maps'),
   path('report/', views.report, name='report'),
   path('eventsAndActivities/', views.eventsAndActivities, name='eventsAndActivities')
 ]
