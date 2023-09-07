from typing import Dict

from django.db import models
from django.http import HttpRequest
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.safestring import mark_safe
from django import template
from django.utils.functional import cached_property
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import (
    gettext as _,
    gettext_lazy as _l,
)

from tinymce.models import HTMLField

from base.mixins import HtmlElementMixin, SiteMixin, TimestampMixin


class File(SiteMixin):
    name = models.CharField(
        _l('name'),
        max_length=100,
    )
    file = models.FileField(
        _l('file'),
        upload_to='files/'
    )
    type = models.CharField(
        _l('type'),
        max_length=10,
    )


class Category(SiteMixin):
    name = models.CharField(
        _l('name'),
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        _l('slug'),
        max_length=100,
        unique=True
    )
    description = models.CharField(
        _l('description'),
        max_length=200,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _l('category')
        verbose_name_plural = _l('categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(SiteMixin):
    name = models.CharField(_l('name'), max_length=50, unique=True)

    class Meta:
        verbose_name = _l('tag')
        verbose_name_plural = _l('tags')
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(SiteMixin, TimestampMixin):
    POST = 'post'
    PAGE = 'page'

    DRAFT = 'draft'
    PUBLISHED = 'published'

    type = models.CharField(
        _l('type'),
        max_length=4,
        default=POST,
        choices=(
            (POST, _l('Post')),
            (PAGE, _l('Page')),
        )
    )
    title = models.CharField(
        _l('title'),
        max_length=200,
    )
    slug = models.SlugField(
        _l('slug'),
        max_length=200,
        unique=True,
        help_text=_l("This will be part of the page URL.")
    )
    content = HTMLField(
        _l('content'),
        blank=True,
    )
    excerpt = models.CharField(
        _l('excerpt'),
        null=True,
        blank=True,
        max_length=500,
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name=_l('categories'),
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_l('tags')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_l('author'),
    )
    published_at = models.DateTimeField(
        _l('published at'),
        null=True,
        blank=True,
    )
    cover_image = models.ForeignKey(
        File,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_l('cover image'),
    )
    order = models.IntegerField(
        _l('order'),
        default=0,
    )
    views = models.PositiveIntegerField(
        _l('views'),
        default=0
    )
    likes = models.PositiveIntegerField(
        _l('likes'),
        default=0,
    )
    status = models.CharField(
        max_length=10,
        choices=(
            (DRAFT, _l('Draft')),
            (PUBLISHED, _l('Published')),
        ),
        default=DRAFT,
    )
    allow_comments = models.BooleanField(
        _l('allow comments'),
        default=True,
    )
    template = models.ForeignKey(
        'Template',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_l('template'),
    )

    class Meta:
        verbose_name = _l('post')
        verbose_name_plural = _l('posts')
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title


class Comment(SiteMixin, TimestampMixin):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _l('comment')
        verbose_name_plural = _l('comments')

    def __str__(self):
        return f'Comment for {self.author} in {self.post}'


class Menu(SiteMixin):
    name = models.CharField(
        _l('name'),
        max_length=100,
        unique=True,
    )
    order = models.IntegerField(
        _l('order'),
        default=0,
    )

    class Meta:
        verbose_name = _l('menu')
        verbose_name_plural = _l('menus')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )
    label = models.CharField(
        _l('label'),
        max_length=100,
    )
    url = models.URLField(
        _l('URL'),
        blank=True,
        null=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_l('post'),
    )
    order = models.IntegerField(
        _l('order'),
        default=0,
    )

    class Meta:
        verbose_name = _l('menu item')
        verbose_name_plural = _l('menu items')

    def __str__(self):
        return self.label


class Widget(SiteMixin):
    identifier = models.SlugField(
        unique=True,
        max_length=50,
    )
    name = models.CharField(
        _l('name'),
        max_length=100,
        unique=True,
    )
    description = models.CharField(
        _l('description'),
        max_length=200,
        blank=True,
    )
    content = models.TextField(
        _l('content'),
    )
    is_active = models.BooleanField(
        _l('is active'),
        default=True,
    )

    class Meta:
        verbose_name = _l('widget')
        verbose_name_plural = _l('widget')

    def __str__(self):
        return self.name


class Section(SiteMixin, HtmlElementMixin):
    HEADER = 'header'
    MAIN = 'main'
    FOOTER = 'footer'

    name = models.CharField(
        _l('name'),
        max_length=50,
    )
    content = HTMLField()
    location = models.CharField(
        _l('location'),
        max_length=10,
        choices=(
            (HEADER, _l('header')),
            (MAIN, _l('main')),
            (FOOTER, _l('footer')),
        )
    )
    is_active = models.BooleanField(
        _l('is_active'),
        default=True,
    )

    class Meta:
        verbose_name = _l('section')
        verbose_name_plural = _l('section')

    def __str__(self):
        return self.name

    @classmethod
    def header(cls):
        return cls.objects.filter(location=cls.HEADER, is_active=True)

    @classmethod
    def main(cls):
        return cls.objects.filter(location=cls.MAIN, is_active=True)

    @classmethod
    def footer(cls):
        return cls.objects.filter(location=cls.FOOTER, is_active=True)

    def render(self, request: HttpRequest = None, context: Dict = None):
        if request:
            context['request'] = request

        django_template = template.Template(self.content)
        django_context = template.Context(context)
        self.rendered_content = django_template.render(context=django_context)
        return self.rendered_content


class Theme(SiteMixin):
    name = models.CharField(
        _l('name'),
        max_length=100,
        unique=True,
    )
    description = models.CharField(
        _l('description'),
        max_length=200,
        blank=True,
    )
    thumbnail = models.ImageField(
        _l('thumbnail'),
        upload_to='themes/thumbnails/',
        blank=True,
        null=True,
    )
    css = models.TextField(blank=True)
    js = models.TextField(blank=True)
    is_active = models.BooleanField(
        _l('is active'),
        default=True,
    )
    default_template = models.ForeignKey(
        'Template',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _l('theme')
        verbose_name_plural = _l('themes')

    templates: models.QuerySet['Template']

    def __str__(self):
        return self.name

    def header(self):
        return Section.objects.filter(location=Section.HEADER, is_active=True)

    def main(self):
        return Section.objects.filter(location=Section.MAIN, is_active=True)

    def footer(self):
        return Section.objects.filter(location=Section.FOOTER, is_active=True)

    def get_default_template(self):
        return (
            self.default_template or
            self.templates.filter(is_active=True).first() or
            Template.objects.filter(is_active=True).first()
        )


# Modelo para representar una plantilla (Template)
class Template(models.Model):
    name = models.CharField(
        _l('name'),
        max_length=100,
        unique=True,
    )
    description = models.CharField(
        _l('description'),
        max_length=200,
        blank=True,
    )
    template_content = models.TextField(blank=True)
    template_file = models.FileField(
        _l('template from file'),
        upload_to='templates/',
        null=True,
        blank=True,
    )
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        related_name='templates',
        verbose_name=_l('theme')
    )
    is_active = models.BooleanField(
        _l('is active'),
        default=True,
    )

    class Meta:
        verbose_name = 'Plantilla'
        verbose_name_plural = 'Plantillas'

    def __str__(self):
        return self.name

    def clean(self):
        try:
            self.render()
        except (ValueError, template.TemplateSyntaxError, AssertionError) as e:
            raise ValidationError(e)

    @cached_property
    def content(self):
        if self.template_content:
            return mark_safe(self.template_content)
        elif self.template_file:
            return mark_safe(self.template_file.read())
        raise ValueError(f'template {self} has no content.')

    def render(self, request: HttpRequest = None, context: Dict = None):
        if request:
            context['request'] = request

        django_template = template.Template(self.content)
        django_context = template.Context(context)
        return django_template.render(context=django_context)



class SiteConfig(SiteMixin):
    site_title = models.CharField(
        _l('site title'),
        max_length=200,
    )
    site_description = models.CharField(
        _l('site description'),
        max_length=500,
    )
    site_logo = models.ForeignKey(
        File,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_l('site logo'),
    )
    favicon = models.ImageField(
        _l('favicon'),
        upload_to='favicon/'
    )
    theme = models.ForeignKey(
        Theme,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    homepage = models.ForeignKey(
        Post,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_l('homepage'),
    )
    comment_form_button_label = models.CharField(
        _l('comment form button label'),
        max_length=100,
        default=_l('Send'),
    )
    comment_form_textarea_cols = models.PositiveSmallIntegerField(
        _l('comment form textarea cols'),
        default=10,
    )
    comment_form_textarea_rows = models.PositiveSmallIntegerField(
        _l('comment form textarea cols'),
        default=3,
    )

    class Meta:
        verbose_name = _l('site config')
        verbose_name_plural = _l('site configs')

    def __str__(self):
        return self.site_title

    @classmethod
    def get_current(cls, request=None):
        site = get_current_site(request)
        return cls.objects.get(site=site)