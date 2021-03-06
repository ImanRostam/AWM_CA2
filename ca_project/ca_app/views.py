from django.shortcuts import render
from django.http import JsonResponse
from googleplaces import GooglePlaces, types
from .models import LocatePlace


# Create your view here


def updateDB(request):
    try:
        lat = request.POST['lat']
        lon = request.POST['lon']

        location = LocatePlace()
        location.lat = lat
        location.lon = lon
        location.save()
        return JsonResponse({"message": "Successfully updated"}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def getPlace(placeType):
    switcher = {
        'restaurant': types.TYPE_RESTAURANT,
        'takeaway': types.TYPE_MEAL_TAKEAWAY,
        'delivery': types.TYPE_MEAL_DELIVERY,
        'bakery': types.TYPE_BAKERY,
        'cafe': types.TYPE_CAFE,
        'supermarket': types.TYPE_GROCERY_OR_SUPERMARKET,
        'store': types.TYPE_STORE,
    }
    return switcher.get(placeType, "Invalid Argument")


def updatePlace(request):
    API_KEY = 'AIzaSyBJsrIufmPtbESCrLMRG4eDmDjlPIa3Fi0'

    try:
        requestPlaceType = request.POST['type']
        currentLat = float(request.POST['lat'])
        currentLng = float(request.POST['lng'])

        names = []
        lat = []
        lng = []
        address = []
        google_places = GooglePlaces(API_KEY)

        if requestPlaceType == 'default':
            return

        query_result = google_places.nearby_search(
            lat_lng={'lat': currentLat, 'lng': currentLng}, keyword="Restaurants",
            radius=3000, types=[getPlace(requestPlaceType)])

        for place in query_result.places:
            print(place.name)
            place.get_details()
            names.append(place.name)
            lat.append(float(place.geo_location['lat']))
            lng.append(float(place.geo_location['lng']))
            address.append(place.formatted_address)

        return JsonResponse({'names': names, 'lat': lat, 'lng': lng, 'address': address}, status=200, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"message": str(e)}, status=400)
