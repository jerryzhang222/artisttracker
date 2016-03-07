"""
Definition of models.
"""

from django.db import models

# Create your models here.


class Artist(models.Model):
    soundcloud_id = models.BigIntegerField()
    permalink = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    uri = models.URLField(max_length=200)
    permalink_url = models.URLField(max_length=200)
    avatar_url = models.URLField(max_length=200)
    country = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    discogs_name = models.CharField(max_length=200)
    myspace_name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    website_title = models.CharField(max_length=200)
    track_count = models.IntegerField()
    playlist_count = models.IntegerField()

    # many to many with itself
    # has many favourites
    pass
    # put the web profiles here too


class Tracks(models.Model):
    # artist has many tracks - artist foreign key
    # has many favouriters
    pass


class Playlist(models.Model):
    # many to many with tracks
    pass


class Comments(models.Model):
    pass


class Groups(models.Model):
    # has many artists
    # has many Tracks
    pass

class 