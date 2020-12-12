from django.shortcuts import render
from django.http import JsonResponse
from googleplaces import GooglePlaces, types, lang
from .models import Locate

# Create your view here


def updatedb(request):
    try:
        lat = request.POST['lat']
        lon = request.POST['lon']

        location = Locate()
        location.lat = lat
        location.lon = lon
        location.save()
        return JsonResponse({"message": "Successfully updated"}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

