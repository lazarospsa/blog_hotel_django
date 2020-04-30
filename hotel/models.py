from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.shortcuts import redirect
from django.utils import timezone

# Create your models here.


class Room(models.Model):
    #room = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField(default=0)
    maxpeople = models.IntegerField(default=1)
    #katoxos = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
    def save(self, *args, **kwargs):#uparxei hdh k trexei automata alla epeidh 9elw na kanw tropopoihseis (na apo9hkeuw tis eikones se mikrotera mege9h) prepei na to kanw xeirografa
        super().save(*args, **kwargs)

        #dhlwnw to path ths photo
        img = Image.open(self.photoroom.path)

        #allazei to mege9os ths fwtografias
        if img.height > 1000 or img.width > 1000:
            output_size = (200, 500)
            img.thumbnail(output_size)
            img.save(self.photoroom.path)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('hotel-room-detail', kwargs={'pk':self.pk})
    
    class Meta:
       verbose_name = 'Room'
       verbose_name_plural = 'Rooms'
