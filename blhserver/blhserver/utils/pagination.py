from rest_framework.pagination import PageNumberPagination


class pageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'limit'
    max_page_size = 100

    def data(self, request, instance, serializerClass):
        pagers = self.paginate_queryset(queryset=instance, request=request)
        serializer = serializerClass(pagers, many=True)
        return {
            'total': len(instance),
            'list': serializer.data,
            'max_page': self.page.paginator.num_pages,
            'now_page': self.page.number,
            'page_size': self.page_size
        }