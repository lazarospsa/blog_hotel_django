from hotel.models import Room
from restapi.serializers import RoomSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer