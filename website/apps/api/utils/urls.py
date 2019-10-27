from collections import OrderedDict

from django.urls import URLPattern


def url_mapping(urls, app_label=None):
    mapped = OrderedDict()
    prefix = app_label + ':' if app_label else ''
    for url in urls:
        if isinstance(url, URLPattern):
            mapped[url.name] = url.name
        else:
            resolver = url
            name = resolver.resolve(resolver.pattern).url_name
            mapped[name] = prefix + name

    return mapped
