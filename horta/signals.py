from django.dispatch import receiver
from django.db.models.signals import post_save
import models

@receiver(post_save, sender=models.Bed)
def update_parcel_geometry(sender, **kwargs):
    bed = kwargs.get('instance')
    bed.parcel.update_geometry()

@receiver(post_save, sender=models.Parcel)
def update_garden_geometry(sender, **kwargs):
    parcel = kwargs.get('instance')
    print('garden: %(garden_name)s - parcel: %(parcel_name)s' % {
        'garden_name' : parcel.garden.name, 
        'parcel_name' : parcel.name
        })
    parcel.garden.update_geometry()
