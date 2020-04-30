from rest_framework import serializers
from .models import Tracker

class TrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'user', 'start_time', 'end_time', )
        model = Tracker

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('start_time', 'endtime')