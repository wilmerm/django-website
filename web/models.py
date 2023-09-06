from django.db import models
from django.conf import settings
from django.utils.translation import (
    gettext as _,
    gettext_lazy as _l,
)

from tinymce.models import HTMLField

from base.mixins import TimestampMixin


class Category(models.Model):
    name = models.CharField(_l('name'), max_length=100, unique=True)
    slug = models.SlugField(_l('slug'), max_length=100, unique=True)
    description = models.TextField(_l('description'), blank=True, null=True)

    class Meta:
        verbose_name = _l('category')
        verbose_name_plural = _l('categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(_l('name'), max_length=50, unique=True)

    class Meta:
        verbose_name = _l('tag')
        verbose_name_plural = _l('tags')
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(TimestampMixin):
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
    cover_image = models.ImageField(
        upload_to='post_covers/',
        null=True,
        blank=True
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


    class Meta:
        verbose_name = _l('post')
        verbose_name_plural = _l('posts')
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title


class Comment(TimestampMixin):
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

    def __str__(self):
        return f'Comment for {self.author} in {self.post}'