from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host('', settings.ROOT_URLCONF, name='default'),
    host('api', 'apps.api.urls', name='api'),
    host('admin', 'website.admin_urls', name='admin'),
)
