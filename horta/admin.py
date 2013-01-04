from django.contrib.gis import admin
from horta import models

class PolygonRepresentationAdmin(admin.GeoModelAdmin):
    pass

class GardenAdmin(admin.ModelAdmin):
    pass

class ParcelAdmin(admin.ModelAdmin):
    pass

class BedAdmin(admin.ModelAdmin):
    pass

class SpeciesAdmin(admin.ModelAdmin):
    pass

class PlantationAdmin(admin.ModelAdmin):
    pass

class WorkSessionAdmin(admin.ModelAdmin):
    pass

class BedPolygonRepresentationAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.PolygonRepresentation, PolygonRepresentationAdmin)
admin.site.register(models.Garden, GardenAdmin)
admin.site.register(models.Parcel, ParcelAdmin)
admin.site.register(models.Bed, BedAdmin)
admin.site.register(models.Species, SpeciesAdmin)
admin.site.register(models.Plantation, PlantationAdmin)
admin.site.register(models.WorkSession, WorkSessionAdmin)
admin.site.register(models.BedPolygonRepresentation, 
                    BedPolygonRepresentationAdmin)
