from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import Pagination_1_Via_PageNumberPagination, Pagination_2_Via_LimitOffsetPagination, Pagination_3_Via_CursorPagination

# Create your views here.


class EmployeeAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # pagination_class = Pagination_1_Via_PageNumberPagination
    # pagination_class = Pagination_2_Via_LimitOffsetPagination
    pagination_class = Pagination_3_Via_CursorPagination
