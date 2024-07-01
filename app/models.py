from django.db import models

class Movie(models.Model):
    
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title + ' ' + self.genre