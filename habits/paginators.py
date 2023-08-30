from rest_framework.pagination import PageNumberPagination


class HabitListPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 50
    page_size_query_param = 'page_size'


class RewardPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10
    page_size_query_param = 'page_size'