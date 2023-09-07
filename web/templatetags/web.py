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
def section(section_obj: Section, request=None, **context):
    assert isinstance(section_obj, Section), f'The "{section_obj}" is not valid section.'

    section_obj.render(request, context)

    return {
        'section': section_obj,
    }


@register.inclusion_tag('tags/widget.html')
def widget(widget_or_identifier: Widget | str):
    if isinstance(widget_or_identifier, str):
        try:
            widget = Widget.objects.get(identifier=widget_or_identifier)
        except Widget.DoesNotExist:
            raise ValueError(f'Widget with identifier "{widget_or_identifier}" does not exist.')
    elif isinstance(widget_or_identifier, Widget):
        widget = widget_or_identifier
    else:
        raise ValueError(f'The "{widget_or_identifier}" is not a valid widget.')

    return {
        'widget': widget,
    }
