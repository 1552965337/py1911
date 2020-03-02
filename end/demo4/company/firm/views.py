from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import viewsets

class BranchViewSets(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class StaffViewSets(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = StaffSerializer