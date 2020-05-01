from rest_framework import serializers
from .models import CustomUser
from tracker.serializers import TrackSerializer

class UserSerializer(serializers.ModelSerializer):
    activities = TrackSerializer(
        many=True,
        read_only=True,
    )
    
    class Meta:
        fields = ('first_name', 'last_name', 'timezone', 'user_id', 'activities',)
        model = CustomUser
