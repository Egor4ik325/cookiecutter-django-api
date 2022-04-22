from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, DynamicRoute, Route, SimpleRouter


class Router(DefaultRouter if settings.DEBUG else SimpleRouter):  # type: ignore
    """Custom API router."""

    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={
                "get": "list",
                "post": "create",
                "delete": "purge",
            },
            name="{basename}_list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}_{url_name}",
            detail=False,
            initkwargs={},
        ),
        Route(
            url=r"^{prefix}/{lookup}{trailing_slash}$",
            mapping={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            },
            name="{basename}_detail",
            detail=True,
            initkwargs={"suffix": "Instance"},
        ),
        DynamicRoute(
            url=r"^{prefix}/{lookup}/{url_path}{trailing_slash}$",
            name="{basename}_{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]


router = Router()

urlpatterns = router.urls
