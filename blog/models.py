from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #Με το User.objects.filter(username='lazarospsa').first() αναζητάει την τιμή lazarospsa
    #μέσα στο User από τα objects και επιστρέφει την first() τιμή.

    #Με αυτή την function επιλέγουμαι ποιο στοιχείο θα φαίνεται όταν γίνεται ένα queryset πάνω στο Post
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
