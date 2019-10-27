from django.urls import path, include
from django_urls import UrlManager
from rest_framework.routers import APIRootView

from .google import google_urls
from ...utils.urls import url_mapping

social_auth_urls = UrlManager()

social_auth_urls.extend([
    path('google/', include((google_urls.url_patterns, 'api'), namespace='google_auth'))
])


@social_auth_urls.path('', name='social_auth')
class SocialAuthentication(APIRootView):
    """Third party authentication endpoints."""
    api_root_dict = url_mapping(social_auth_urls.url_patterns, 'api')
