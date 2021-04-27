from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


"""

Audio model with 
ID – (mandatory, integer, unique)
Name of the song – (mandatory, string, cannot be larger than 100
characters)
Duration in number of seconds – (mandatory, integer, positive)
Uploaded time – (mandatory, Datetime, cannot be in the past)

"""
class Audio(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

"""

Podcast model with
ID – (mandatory, integer, unique)
Name of the podcast – (mandatory, string, cannot be larger than 100
characters)
Duration in number of seconds – (mandatory, integer, positive)
Uploaded time – (mandatory, Datetime, cannot be in the past)
Host – (mandatory, string, cannot be larger than 100 characters)
Participants – (optional, list of strings, each string cannot be larger than
100 characters, maximum of 10 participants possible)

"""

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=10,
        )

    def __str__(self):
        return self.name


"""

Audiobook model with 
ID – (mandatory, integer, unique)
Title of the audiobook – (mandatory, string, cannot be larger than 100
characters)
Author of the title (mandatory, string, cannot be larger than 100
characters)
Narrator - (mandatory, string, cannot be larger than 100 characters)
Duration in number of seconds – (mandatory, integer, positive)
Uploaded time – (mandatory, Datetime, cannot be in the past)

"""
class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title