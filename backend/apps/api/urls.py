from django.urls import path, include
from django_urls import UrlManager
from rest_auth.registration.urls import urlpatterns as _rest_auth_registration_urls
from rest_auth.urls import urlpatterns as _rest_auth_urls
from rest_framework.routers import APIRootView

from . import views
from .router import RooterWithUrls
from .utils.urls import url_mapping

router = RooterWithUrls()
router.register(r'resources', views.ResourceViewSet, basename='resource')
router.register(r'telegram', views.TelegramGroupViewSet, 'telegram')

rest_auth_registration_urls = UrlManager()
rest_auth_registration_urls.extend(_rest_auth_registration_urls)

rest_auth_urls = UrlManager()
rest_auth_urls.extend(_rest_auth_urls)


@rest_auth_registration_urls.path('', name='auth_registration')
class Registration(APIRootView):
    """Registration endpoints."""
    api_root_dict = url_mapping(rest_auth_urls.url_patterns)


rest_auth_urls.extend([path('registration/', include(rest_auth_registration_urls.url_patterns))])


@rest_auth_urls.path('', name='auth')
class Authentication(APIRootView):
    """Authentication endpoints."""
    api_root_dict = url_mapping(rest_auth_urls.url_patterns)


urlpatterns = [
    path('social_auth/', include(views.social_auth_urls.url_patterns)),
    path('auth/', include(rest_auth_urls.url_patterns)),
]

router.register_extra_urls(urlpatterns)

urlpatterns += [
    path('', include(router.urls))
]

