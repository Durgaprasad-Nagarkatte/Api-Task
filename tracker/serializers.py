from rest_framework import serializers
from .models import Tracker

class TrackSerializer(serializers.ModelSerializer):
    class Meta:

        extra_kwargs = {
            'id': {'write_only': True},
            'user' : {'write_only' : True},

        }
        fields = ('start_time', 'end_time',)
        model = Tracker

"""
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('start_time', 'endtime')
"""