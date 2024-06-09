from django import template


register = template.Library()

@register.simple_tag
def filter_and_paginate(field_name: str, value, urlencode=None):
    url = f"?{field_name}={value}"
    if urlencode is None:
        return url
    
    a = urlencode.split("&")
    a = filter(lambda p: p.split("=")[0]!=field_name, a)
    a = "&".join(a)
    url = f"{url}&{a}"
    return url