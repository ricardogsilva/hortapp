from tastypie.resources import ModelResource
from tastypie import fields
import horta.models

class GardenResource(ModelResource):
    class Meta:
        queryset = horta.models.Garden.objects.all()
        resource_name = 'garden'

class BedResource(ModelResource):
    class Meta:
        queryset = horta.models.Bed.objects.all()
        resource_name = 'bed'

class SpeciesResource(ModelResource):
    class Meta:
        queryset = horta.models.Species.objects.all()
        resource_name = 'species'

class PlantationResource(ModelResource):
    bed = fields.ForeignKey(BedResource, 'zone')#, full=True)
    species = fields.ForeignKey(SpeciesResource, 'species')

    class Meta:
        queryset = horta.models.Plantation.objects.all()
        resource_name = 'plantation'
