from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),
   path('', views.home, name='home'),
   path('create-report', views.createReport, name="create-report"),
    path('read-report', views.readReport, name="read-report"),
    path('read-report/<str:pk>', views.readReport, name="read-report"),
    path('update-report/<str:pk>', views.updateReport, name="update-report"),
    path('delete-report/<str:pk>', views.deleteReport, name="delete-report"),

   path('maps/', views.maps, name='maps'),
   path('report/', views.report, name='report'),
   path('eventsAndActivities/', views.eventsAndActivities, name='eventsAndActivities')
 ]
