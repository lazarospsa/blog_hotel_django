from django.shortcuts import render
from hotel.models import Room
from restapi.serializers import RoomSerializer
from rest_framework import generics

# Create your views here.

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer