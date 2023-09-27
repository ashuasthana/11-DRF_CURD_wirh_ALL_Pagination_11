from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class Pagination_1_Via_PageNumberPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'mypage'  # Default value is 'page'
    page_size_query_param = 'num'
    max_page_size = 11
    last_page_strings = ('end_page',)  # Default value is ('last',)


class Pagination_2_Via_LimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
    limit_query_param = 'mylimit'  # Default value is 'limit'
    offset_query_param = 'myoffset'  # Default value is 'offset'
    max_limit = 11


class Pagination_3_Via_CursorPagination(CursorPagination):
    ordering = '-esal'  # based on descending order of employee salaryes
    page_size = 5
    cursor_query_param = 'mycursor '
