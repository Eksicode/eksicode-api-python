from rest_framework.pagination import PageNumberPagination


def custom_paginator(**kwargs):
    kwargs.setdefault('page_size', 10)
    kwargs.setdefault('page_query_param', 'page')
    kwargs.setdefault('page_size_query_param', 'page_size')
    kwargs.setdefault('max_page_size', 50)

    class CustomPaginator(PageNumberPagination):
        ...

    for attr, val in kwargs.items():
        setattr(CustomPaginator, attr, val)

    return CustomPaginator
