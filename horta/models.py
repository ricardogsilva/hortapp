from django.db import models
from django.contrib.gis.db import models as geo_models

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class GeoRepresentation(geo_models.Model):
    item = geo_models.ForeignKey(Item)

class PolygonRepresentation(GeoRepresentation):
    objects = geo_models.GeoManager()
    geom = geo_models.PolygonField()

class Zone(Item):
    name = models.CharField(max_length=100, default='Zone')

class Canteiro(Zone):
    pass

