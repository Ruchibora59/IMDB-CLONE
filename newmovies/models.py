from django.db import models

# Create your models here.

class Upcoming(models.Model):

    name = models.CharField(max_length=70,unique=True)
    release_date = models.DateField()
    description = models.CharField(max_length=2000)
    picture = models.ImageField(upload_to = 'upcome/img')


    def __str__(self):
        return self.name


    


