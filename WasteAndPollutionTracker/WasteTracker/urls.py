from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('maps/', views.maps, name='maps'),

    # rename this to avoid conflict
    path('report/', views.report_page, name='report'),

    # CREATE
    path('create-report/', views.createReport, name="create-report"),

    # READ ALL (list page)
    path('reports/', views.home, name="read-reports"),

    # READ ONE
    path('report/<str:pk>/', views.readReport, name="read-report"),

    # UPDATE
    path('update-report/<str:pk>/', views.updateReport, name="update-report"),

    # DELETE
    path('delete-report/<str:pk>/', views.deleteReport, name="delete-report"),

    path('eventsAndActivities/', views.eventsAndActivities, name='eventsAndActivities')
]