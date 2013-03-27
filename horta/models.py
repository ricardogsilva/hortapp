from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import MultiPolygon

class Media(models.Model):
    the_file = models.FileField(upload_to='tmp', verbose_name='file')

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    files = models.ManyToManyField(Media, null=True, blank=True)

    def __unicode__(self):
        try:
            the_name = self.name
        except AttributeError:
            the_name = 'item'
        return the_name

class Garden(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    name = models.CharField(max_length=100)
    geom = models.PointField(editable=False, null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    def update_geometry(self):
        '''
        Automatically update geometry based on the geometries of own Parcels.
        '''

        mp = MultiPolygon([p.geom for p in self.parcel_set.all() if \
                p.geom is not None])
        if not mp.empty:
            self.geom = mp.centroid
            self.save()

class Parcel(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    garden = models.ForeignKey(Garden)
    name = models.CharField(max_length=100, default='Parcel')
    geom = models.PolygonField(editable=False, null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    def update_geometry(self):
        '''
        Automatically update geometry based on the geometries of own Zones.
        '''

        mp = MultiPolygon([z.geom for z in self.zone_set.all()])
        if not mp.empty:
            self.geom = mp.convex_hull
            self.save()

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
    objects = models.GeoManager()

class Species(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    name = models.CharField(max_length=100, default='unspecified')
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'species'

    def __unicode__(self):
        return self.name

class Plantation(Item):
    species = models.ForeignKey(Species)
    zone = models.ForeignKey(Zone)

    def __unicode__(self):
        info = {'zone' : self.zone.name, 
                'species' : self.species.name}
        return '%(zone)s - %(species)s' % info

class Meeting(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    date_time = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

class WorkSession(Meeting):
    zones = models.ManyToManyField(Zone, null=True, blank=True)

class Report(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    worksession = models.ForeignKey(WorkSession)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class Task(Item):
    STATUS_CHOICES = (
        ('not started', 'not started'),
        ('in progress', 'in progress'),
        ('finished', 'finished'),
    )
    item = models.OneToOneField(Item, primary_key=True, parent_link=True)
    title = models.CharField(max_length=100)
    zones = models.ManyToManyField(Zone, null=True, blank=True)
    author = models.ForeignKey(User, related_name='task_author')
    assigned_to = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __unicode__(self):
        return self.title
