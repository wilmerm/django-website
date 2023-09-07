
from django.contrib.sites.shortcuts import get_current_site

from .models import SiteConfig, Widget


def context(request):
    site = get_current_site(request)

    return {
        'site': site,
    }