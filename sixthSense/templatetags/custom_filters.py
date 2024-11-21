from django import template

register = template.Library()

@register.filter
def get_yes_no(value):
    return "Yes" if value else "No"