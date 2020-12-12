from django.urls import path
from . import views

urlpatterns = [
    path('updatedb/', views.updatedb, name='updatedb'),
]