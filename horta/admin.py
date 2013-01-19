from django.contrib.gis import admin
from horta import models

class ItemMediaInline(admin.StackedInline):
    model = models.Item.files.through
    extra = 1

class MediaAdmin(admin.ModelAdmin):
    pass

class GenericItemAdmin(admin.ModelAdmin):
    inlines = [ItemMediaInline]
    exclude = ['files']

class GardenAdmin(GenericItemAdmin):
    pass

class ParcelAdmin(GenericItemAdmin):
    pass

class SpeciesAdmin(GenericItemAdmin):
    pass

class PlantationAdmin(GenericItemAdmin):
    pass

class MeetingAdmin(GenericItemAdmin):
    pass

class WorkSessionAdmin(GenericItemAdmin):
    pass

class ReportAdmin(GenericItemAdmin):
    pass

class TaskAdmin(GenericItemAdmin):
    pass

class BedAdmin(admin.GeoModelAdmin, GenericItemAdmin):
    pass

admin.site.register(models.Garden, GardenAdmin)
admin.site.register(models.Parcel, ParcelAdmin)
admin.site.register(models.Bed, BedAdmin)
admin.site.register(models.Species, SpeciesAdmin)
admin.site.register(models.Plantation, PlantationAdmin)
admin.site.register(models.Meeting, MeetingAdmin)
admin.site.register(models.WorkSession, WorkSessionAdmin)
admin.site.register(models.Report, ReportAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Media, MediaAdmin)
