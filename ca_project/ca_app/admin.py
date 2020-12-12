from django.contrib.gis import admin
from .models import WorldBorder, LocatePlace

# register your models here

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(LocatePlace, admin.GeoModelAdmin)
