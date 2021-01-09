from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="domain_name")
@stringfilter
def domain_name(value):
    return value.split("//")[-1].split("/")[0].replace("www.", "")
