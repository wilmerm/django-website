from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.db.models.query import QuerySet
from django.utils.translation import gettext as _, gettext_lazy as _l


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OnSiteManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        site = get_current_site(None)
        return super().get_queryset().filter(site=site)


class SiteMixin(models.Model):
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        editable=False,
    )

    objects = OnSiteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.site = get_current_site(None)
        super().save(*args, **kwargs)


class HtmlElementMixin(models.Model):
    ALLOWED_ATTR_NAMES = [
        'id',
        'class',
        'style',
        'name',
        'value',
        'min',
        'max',
        'min_lenght',
        'max_lenght',
    ]
    attrs = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.validate_attrs()
        super().save(*args, **kwargs)

    def validate_attrs(self):
        if self.attrs:
            for key, value in self.attrs.items():
                if value != None and not key in self.ALLOWED_ATTR_NAMES:
                    raise ValueError(_('Attr "%s" is not allowd.') % key)