from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        try:
            the_name = self.name
        except AttributeError:
            the_name = 'item'
        return the_name

class Garden(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Parcel(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    garden = models.ForeignKey(Garden)
    name = models.CharField(max_length=100, default='Parcel')

    def __unicode__(self):
        return self.name

class Zone(Item):

    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    parcel = models.ForeignKey(Parcel)
    name = models.CharField(max_length=100, default='Zone')
    geom = models.PolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Bed(Zone):
    zone = models.OneToOneField(Zone, primary_key=True, parent_link=True)

class Species(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    name = models.CharField(max_length=100, default='unspecified')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'species'

    def __unicode__(self):
        return self.name

class Plantation(models.Model):
    species = models.ForeignKey(Species)
    zone = models.ForeignKey(Zone)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        info = {'zone' : self.zone.name, 
                'species' : self.species.name}
        return '%(zone)s - %(species)s' % info

class WorkSession(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    zones = models.ManyToManyField(Zone)
    date_time = models.DateTimeField()
    description = models.TextField()
    users = models.ManyToManyField(User)
