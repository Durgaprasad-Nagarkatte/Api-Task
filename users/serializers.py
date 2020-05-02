from rest_framework import serializers
from .models import CustomUser
from tracker.serializers import TrackSerializer


class UserSerializer(serializers.ModelSerializer):
    activities = TrackSerializer(
        many=True,
        read_only=True,
    )
    real_name = serializers.SerializerMethodField()
    
    class Meta:
        extra_kwargs = {
            'id': {'write_only': True},
            'first_name' : {'write_only' : True},
            'last_name' : {'write_only' : True},
        }
        validators = []

        fields = ('first_name', 'last_name', 'timezone', 'user_id', 'activities', 'real_name')
        model = CustomUser


    def get_real_name(self, obj):
        return obj.first_name + " " + obj.last_name
