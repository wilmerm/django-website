from django import template

from ..models import (
    Post,
    Section,
    Widget,
)


register = template.Library()


@register.inclusion_tag('tags/comment_form.html')
def comment_box(post: Post):
    return {
        'post': post,
    }


@register.inclusion_tag('tags/section.html')
def section(section: Section):
    return {
        'section': section,
    }


@register.inclusion_tag('tags/widget.html')
def widget(widget: Widget):
    return {
        'widget': widget,
    }
