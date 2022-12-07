from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_tasks': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })