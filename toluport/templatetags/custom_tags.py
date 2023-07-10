from django import template

register = template.Library()

@register.filter
def split_tags(value):
    return value.split(",")
