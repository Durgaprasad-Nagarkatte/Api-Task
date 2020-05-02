from rest_framework import serializers
from .models import Tracker
from datetime import datetime
from pytz import timezone

class TrackSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        print("Reached here")
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("finish must occur after start")
        return data

    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        extra_kwargs = {
            'id': {'write_only': True},
            'user' : {'write_only' : True},
            'start_utc_time' : {'write_only':True},
            'end_utc_time': {'write_only':True}
        }

        fields = ('user', 'start_utc_time', 'end_utc_time', 'start_time', 'end_time',)
        model = Tracker

    def get_start_time(self, obj):
        new_time_zone = timezone(obj.user.timezone)
        new_time = obj.start_utc_time.astimezone(new_time_zone)
        return new_time.strftime("%b %d %Y %I:%M%p")

    def get_end_time(self, obj):
        new_time_zone = timezone(obj.user.timezone)
        new_time = obj.end_utc_time.astimezone(new_time_zone)
        return new_time.strftime("%b %d %Y %I:%M%p")

