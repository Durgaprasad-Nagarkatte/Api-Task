from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tracker
from .serializers import TrackSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackSerializer
