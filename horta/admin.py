from django.contrib.gis import admin
from horta import models

class GardenAdmin(admin.ModelAdmin):
    pass

class ParcelAdmin(admin.ModelAdmin):
    pass

class BedAdmin(admin.GeoModelAdmin):
    pass

class SpeciesAdmin(admin.ModelAdmin):
    pass

class PlantationAdmin(admin.ModelAdmin):
    pass

class WorkSessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Garden, GardenAdmin)
admin.site.register(models.Parcel, ParcelAdmin)
admin.site.register(models.Bed, BedAdmin)
admin.site.register(models.Species, SpeciesAdmin)
admin.site.register(models.Plantation, PlantationAdmin)
admin.site.register(models.WorkSession, WorkSessionAdmin)
