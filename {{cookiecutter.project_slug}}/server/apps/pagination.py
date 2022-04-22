from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    """API page number-based pagination."""

    page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
    max_page_size = settings.REST_FRAMEWORK["MAX_PAGE_SIZE"]
    page_query_param = settings.REST_FRAMEWORK["PAGE_PARAM"]
    page_size_query_param = settings.REST_FRAMEWORK["PAGE_SIZE_PARAM"]
