'''
auto to arxeio to eftia3a gia na <<stelnei shma>> otan
apo9hkeuoume kati na kanei kati allo
paradeigma automata na dhmiourgei profile otan kapoios kanei eggrafh
'''
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile

'''
decorator @receiver

when a user saved then send this signal and the receiver
create this function with this parametres (sender, instance, created, **kwargs)
so, if that user is created then create the profile object with the user instance infos
'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

'''
save the profile
'''
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()