from tastypie.resources import ModelResource
import horta.models

class GardenResource(ModelResource):
    class Meta:
        queryset = horta.models.Garden.objects.all()
        resource_name = 'garden'
