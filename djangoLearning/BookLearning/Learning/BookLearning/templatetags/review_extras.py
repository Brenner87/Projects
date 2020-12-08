from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name='mycustomlower',is_safe=True)
@stringfilter
def mycustomlower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter(is_safe=True)
@stringfilter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')