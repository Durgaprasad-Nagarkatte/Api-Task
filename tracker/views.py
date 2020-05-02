from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tracker
from .serializers import TrackSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TrackerList(APIView):
    def get(self, request, format=None):
        tracker = Tracker.objects.all()
        serializer = TrackSerializer(tracker, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        print(data)
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class TrackerList(generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackSerializer
"""

class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackSerializer

