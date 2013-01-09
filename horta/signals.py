from django.dispatch import receiver
from django.db.models.signals import post_save
import models

@receiver(post_save, sender=models.Bed)
def update_parcel_geometry(sender, **kwargs):
    bed = kwargs.get('instance')
    bed.parcel.update_geometry()
