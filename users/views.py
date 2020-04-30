from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from tracker.models import Tracker
from rest_framework.response import Response
from tracker.serializers import ActivitySerializer


class UserList(generics.ListCreateAPIView):

    def get(self, request, format=None):
        queryset = CustomUser.objects.all()
        members = []
        for q in queryset:
            info = {}
            info['real_name'] = q.first_name
            info['id'] = q.user_id
            info['tz'] = q.timezone
            acts = []
            activities = Tracker.objects.filter(user=q)
            if(activities):
                for a in activities:
                    acts.append({'start_time' : a.start_time, 'end_time': a.end_time})
            info["activity_periods"] = acts
            members.append(info)
        return Response(members)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer