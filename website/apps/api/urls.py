from django.urls import path, include

from . import views
from .router import RooterWithUrls

router = RooterWithUrls()
router.register(r'resources', views.ResourceViewSet, basename='resource')

urlpatterns = [
    path('', include(router.urls)),
]
