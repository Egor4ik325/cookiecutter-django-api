from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings


class Pagination(PageNumberPagination):
    """API page number-based pagination."""

    page_size = api_settings.PAGE_SIZE
    max_page_size = api_settings.MAX_PAGE_SIZE
    page_query_param = api_settings.PAGE_PARAM
    page_size_query_param = api_settings.PAGE_SIZE_PARAM
