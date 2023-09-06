

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.sites.models import Site

from .models import SiteConfig


@receiver(post_save, sender=Site)
def create_siteconfig(sender, instance, created, **kwargs):
    if created:
        SiteConfig.objects.create(site=instance)