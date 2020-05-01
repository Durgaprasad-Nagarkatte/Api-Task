from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tracker
from .serializers import TrackSerializer


class TrackerList(generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackSerializer
