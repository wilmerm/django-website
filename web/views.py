from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import (
    SiteConfig,
    Widget,
)


def index(request):
    siteconfig = SiteConfig.get_current(request)
    post = siteconfig.homepage
    theme = siteconfig.theme
    widgets = Widget.objects.all()

    context = {
        'post': siteconfig.homepage,
        'theme': theme,
        'siteconfig': siteconfig,
        'widgets': widgets,
    }

    if post and post.template:
        template = post.template
    else:
        template = theme.get_default_template()

    if template:
        html_content = template.render(request, context)
        return HttpResponse(html_content)

    return render(request, 'web/post_detail.html', context)