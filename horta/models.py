from django.contrib.gis.db import models

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class GeoRepresentation(models.Model):
    item = models.ForeignKey(Item)

class PolygonRepresentation(GeoRepresentation):
    geo_representation = models.OneToOneField(GeoRepresentation,
                                              primary_key=True,
                                              parent_link=True)
    objects = models.GeoManager()
    geom = models.PolygonField()

class Zone(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    name = models.CharField(max_length=100, default='Zone')

class Canteiro(Zone):
    zone = models.OneToOneField(Zone, primary_key=True, parent_link=True)

class Especie(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    name = models.CharField(max_length=100, default='unspecified')

class Plantacao(models.Model):
    especie = models.ForeignKey(Especie)
    zone = models.ForeignKey(Zone)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
