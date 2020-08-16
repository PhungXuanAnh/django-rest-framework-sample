import debugpy
from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        debugpy.breakpoint()
        
        return Response(OrderedDict([
            ('current_page', self.page.number),
            ('total_pages', self.page.paginator.num_pages),
            ('total_items', self.page.paginator.count),
            ('data', data),
        ]))
