from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('first_name', 'last_name', 'timezone', 'user_id',)
        model = CustomUser