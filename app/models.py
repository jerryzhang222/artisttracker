"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Artist(models.Model):
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