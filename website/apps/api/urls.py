from django.urls import path, include

from . import views
from .router import RooterWithUrls

router = RooterWithUrls()
router.register(r'resources', views.ResourceViewSet, basename='resource')
router.register(r'telegram', views.TelegramGroupViewSet, 'telegram')

urlpatterns = [
    path('', include(router.urls)),
]
