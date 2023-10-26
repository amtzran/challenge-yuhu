from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class AppPagination(PageNumberPagination):
    """
    Pagination Class for deliveries endpoint
    """

    page_size = 50
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "total": self.page.paginator.count,
                "page": self.page.number,
                "page_size": self.get_page_size(self.request),
                "results": data,
            }
        )
