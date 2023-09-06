
from .models import SiteConfig
from django.contrib.sites.shortcuts import get_current_site


def context(request):
    site = get_current_site(request)
    siteconfig = SiteConfig.objects.get(site=site)
    return {
        'site': site,
        'siteconfig': siteconfig,
        'theme': siteconfig.theme,
    }