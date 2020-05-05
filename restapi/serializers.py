from rest_framework import serializers
from hotel.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta():
        model = Room
        fields = ['title', 'description', 'price', 'maxpeople', 'tetragwnika', 'roomtypes', 'is_reserved']