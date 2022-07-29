from lib2to3.pgen2.parse import ParseError

from django.shortcuts import render
from django.urls import re_path
from django.views.static import serve

from djangoProject1 import settings
from .serializers import *
# Create your views here.
from rest_framework.generics import ListCreateAPIView
from django.views.generic import ListView
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser


class viewuser(ListCreateAPIView):
    queryset = modelusers.objects.all()
    serializer_class = userserializer
class showdocters(ListView):
    queryset = modelusers.objects.filter(Medicalsystemnumber__isnull=False)

class viewtimedoctor(ListCreateAPIView):
    queryset = modeltimedoctor.objects.all()
    serializer_class = timedoctorserializer
class viewmessages(ListCreateAPIView):
    queryset = modelmessages.objects.all()
    serializer_class = messagesserializer