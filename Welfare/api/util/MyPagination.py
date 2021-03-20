from rest_framework.pagination import PageNumberPagination


class Mypage(PageNumberPagination):
    page_size = 8
    # page_query_param = 'pageSize'
    # 定制传参
    page_size_query_param = 'pageSize'
    # 最大一页的数据
    max_page_size = 10