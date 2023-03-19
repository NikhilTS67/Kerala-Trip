from django.urls import path
from . import views

app_name = 'TripApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:ID>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('edit/<int:ID>/', views.edit, name='edit'),
    path('delete/<int:ID>/', views.delete, name='delete'),

]