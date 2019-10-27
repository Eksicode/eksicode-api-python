from collections import OrderedDict

from rest_framework.routers import DefaultRouter

from .utils.urls import url_mapping


class RooterWithUrls(DefaultRouter):
    class APIRootView(DefaultRouter.APIRootView):
        """API endpoints."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra_urls = []

    def register_extra_urls(self, urls):
        self.extra_urls += urls

    def get_api_root_view(self, api_urls=None):
        """
        This is here so we can extend the root view without touching what it provides us with
        """

        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        api_root_dict = OrderedDict({**api_root_dict, **url_mapping(self.extra_urls)})
        return self.APIRootView.as_view(api_root_dict=api_root_dict)
