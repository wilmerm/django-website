from django.contrib import admin

from .models import (
    File,
    Category,
    Tag,
    Post,
    Comment,
    Widget,
    Section,
    Theme,
    Template,
    SiteConfig,
)


class FileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
        'type',
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'description',
    ]
    search_fields = [
        'name',
        'slug',
        'description',
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'type',
        'author',
        'published_at',
        'created_at',
        'updated_at',
        'order',
        'views',
        'likes',
        'allow_comments',
    ]
    readonly_fields = [

    ]
    search_fields = [

    ]
    list_filter = [

    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [

    ]
    readonly_fields = [

    ]
    search_fields = [

    ]
    list_filter = [

    ]


class WidgetAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_active',
    ]
    readonly_fields = [

    ]
    search_fields = [

    ]
    list_filter = [

    ]


class SectionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'location',
        'is_active',
    ]
    readonly_fields = [

    ]
    search_fields = [
        'name',
    ]
    list_filter = [
        'location',
        'is_active',
    ]


class ThemeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_active',
    ]
    readonly_fields = [

    ]
    search_fields = [
        'name',
        'description',
    ]
    list_filter = [
        'is_active',
    ]


class TemplateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    readonly_fields = [

    ]
    search_fields = [

    ]
    list_filter = [

    ]

class SiteConfigAdmin(admin.ModelAdmin):
    list_display = [
        'site',
        'site_title',
    ]
    readonly_fields = [

    ]
    search_fields = [

    ]
    list_filter = [

    ]


admin.site.register(File, FileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Widget, WidgetAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SiteConfig, SiteConfigAdmin)