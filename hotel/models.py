from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.shortcuts import redirect
from django.utils import timezone

class Room(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField(default=0)
    maxpeople = models.IntegerField(default=1)
    photoroom = models.ImageField(default='defaultroom.jpg',upload_to='room_pictures') #sthn metavlhth photoroom orizoume default eikona thn default.jpg kai vazoume upload_to ton fakelo opou 9a apo9hkeuontai
    photodesc = models.CharField(max_length=250, default='This is the room!')
    tetragwnika = models.IntegerField(default=0)
    STUDIO_T = 'Studio'
    DOUBLE_T = 'Double'
    FAMILY_T = 'Family'
    ROOM_TYPES = [
        (STUDIO_T, 'Studio'),
        (DOUBLE_T, 'Double'),
        (FAMILY_T, 'Family'),
    ]
    roomtypes = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
        default=STUDIO_T,
    )
    is_reserved = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photoroom.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (200, 500)
            img.thumbnail(output_size)
            img.save(self.photoroom.path)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('hotel-room-detail', kwargs={'pk':self.pk})
    
    class Meta():
       verbose_name = 'Room'
       verbose_name_plural = 'Rooms'


class Booking(models.Model):
    datein = models.DateField(default=timezone.now)
    dateout = models.DateField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer.username} booking the {self.room_id} at {self.date_posted:%d %B, %Y. %I:%M:%S %p}'
    
    def get_absolute_url(self):
        return reverse('hotel-thanks')