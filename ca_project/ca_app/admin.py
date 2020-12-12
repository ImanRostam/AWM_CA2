from django.contrib.gis import admin
from .models import WorldBorder, Locate

# register your models here

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Locate, admin.GeoModelAdmin)