from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
'''
sthn class Profile 9a kanoume extend to model User tou django gia na exei parapanw pedia
apo auta p dinei to django
paradeigma: photo profile
gia na xrhsimopoihsoume photo sthn efarmogh mas prepei na kanoume pip install Pillow
opou pillow einai ena app opou mporei na diaxeiristei fotografies
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #vazoume to original model
    photoprofile = models.ImageField(default='default.jpg',upload_to='profile_pictures') #sthn metavlhth photoprofile orizoume default eikona thn default.jpg kai vazoume upload_to ton fakelo opou 9a apo9hkeuontai

    def __str__(self): #mas dinei stoixeia gia to ti einai anti gia na leei profile_object
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):#uparxei hdh k trexei automata alla epeidh 9elw na kanw tropopoihseis (na apo9hkeuw tis eikones se mikrotera mege9h) prepei na to kanw xeirografa
        super().save(*args, **kwargs)

        img = Image.open(self.photoprofile.path)

        #allazei to mege9os ths fwtografias
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photoprofile.path)