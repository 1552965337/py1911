# author sqz
# date 2020/3/4 14:48
# file_name pagination
from rest_framework import pagination

class Mypagrnation(pagination.PageNumberPagination):
    page_size =3
    page_query_param="p"
    page_size_query_param="num"