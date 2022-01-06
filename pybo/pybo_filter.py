from django import template

register = template.Libary()


@register.filter
def sub(value, arg):
    return value - arg
