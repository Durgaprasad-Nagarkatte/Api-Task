from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from tracker.models import Tracker
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

"""
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
"""
"""
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
"""

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        print(type(serializer))
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    #Retrieve, update or delete a User instance.
    
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
"""

"""
class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
"""