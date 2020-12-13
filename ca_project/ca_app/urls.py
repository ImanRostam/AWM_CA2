from django.urls import path
from . import views

urlpatterns = [
    path('updateDB/', views.updateDB, name='updateDB'),
    path('updatePlace/', views.updatePlace, name='updatePlace'),
]
