from django.shortcuts import render

from .models import (
    SiteConfig,
)


def index(request):
    siteconfig = SiteConfig.get_current(request)
    context = {
        'post': siteconfig.homepage,
    }
    return render(request, 'web/post_detail.html', context)