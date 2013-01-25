from tastypie.resources import ModelResource
from tastypie import fields
import tastypie.constants as constants
from tastypie.contrib.gis.resources import ModelResource as gis_ModelResource
import horta.models

class MediaResource(ModelResource):
    class Meta:
        queryset = horta.models.Media.objects.all()

class GardenResource(ModelResource):
    #files = fields.ManyToManyField(MediaResource, 'files')
    class Meta:
        always_return_data = True
        queryset = horta.models.Garden.objects.all()
        resource_name = 'garden'
        fields = ['id', 'name']

class ParcelResource(ModelResource):
    class Meta:
        queryset = horta.models.Parcel.objects.all()
        resource_name = 'parcel'

class ZoneResource(ModelResource):
    class Meta:
        queryset = horta.models.Zone.objects.all()
        resource_name = 'zone'
        filtering = {
            'name' : constants.ALL,
        }

class BedResource(gis_ModelResource):
    class Meta:
        queryset = horta.models.Bed.objects.all()
        resource_name = 'bed'
        filtering = {
            'geom' : constants.ALL,
        }

class SpeciesResource(ModelResource):
    class Meta:
        queryset = horta.models.Species.objects.all()
        resource_name = 'species'
        filtering = {
            'name' : constants.ALL_WITH_RELATIONS,
        }

class PlantationResource(ModelResource):
    bed = fields.ForeignKey(BedResource, 'zone')#, full=True)
    species = fields.ForeignKey(SpeciesResource, 'species')

    class Meta:
        queryset = horta.models.Plantation.objects.all()
        resource_name = 'plantation'
        filtering = {
            'species' : constants.ALL_WITH_RELATIONS,
            'bed' : constants.ALL_WITH_RELATIONS,
        }

class WorkSessionResource(ModelResource):
    zones = fields.ManyToManyField(ZoneResource, 'zones')
    class Meta:
        queryset = horta.models.WorkSession.objects.all()
        resource_name = 'worksession'
