from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Programmer, Group
from .serializers import LanguageSerializer, GroupSerializer, ProgrammerSerializer


# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

