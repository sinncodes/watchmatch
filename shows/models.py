from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Show(models.Model):
    name = models.CharField(max_length=50)#increase max length if any title gets cropped
    genres = models.ManyToManyField(Genre)
    rating = models.IntegerField()
     # pg - make this into a choices via pg rating stuff
    release_date = models.DateField()
 
class Interaction(models.Model):
 #   interactions = m
    whenswiped = models.DateField()