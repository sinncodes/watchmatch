from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Show(models.Model):
    name = models.CharField(max_length=50)#increase max length if any title gets cropped
    genre = models.ManyToManyField(Genre)
    score = models.FloatField()
    pg_rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.genre} {self.score} {self.pg_rating} {self.release_date}"
 
class Interaction(models.Model):
    LIKED = "L"
    DISLIKED = "D"

    ACTION_CHOICES = [
        (LIKED, "Liked"),
        (DISLIKED, "Dislike"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    date_swiped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.show}"