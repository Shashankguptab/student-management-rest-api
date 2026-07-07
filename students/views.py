from django.shortcuts import render
from rest_framework import viewsets,filters
from students.models import Student
from students.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from students.pagination import StuentPagination
from students.permissions import IsAdminOrReadOnly
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=StuentPagination

    # easy way for permissions
    # permission_classes=[permissions.IsAuthenticated] ##########Every authenticated user has full access,Only users with a valid token can perform any action.
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]##########Read for everyone, write for authenticated users
    # permission_classes = [permissions.IsAdminUser]######Only admin

    #professional way from permissions.py
    # permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [AllowAny]

    filter_backends=[
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields=['name',
                   'email',
                   'course',
                   ]

    filterset_fields=[
        'course',
        'age',
    ]


    ordering_fields=[
        'name',
        'age',
        'created_at'
    ]

    ordering=['name']

    

    
