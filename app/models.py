"""
Definition of models.
"""

from django.db import models
import mongoengine as me
import mongoengine.fields as fields


# Create your models here.


class Employee(me.Document):
    email = fields.StringField(require=True)
    first_name = fields.StringField(max_length=50)
    last_name = fields.StringField(max_length=50)


class Artist(me.Document):
    # As per the standard soundcloud /users call
    soundcloud_id = fields.LongField(require=True)
    permalink = fields.StringField(max_length=200)
    username = fields.StringField(max_length=200)
    uri = fields.URLField(max_length=200)
    permalink_url = fields.URLField(max_length=200)
    avatar_url = fields.URLField(max_length=200)
    country = fields.StringField(max_length=200)
    full_name = fields.StringField(max_length=200)
    city = fields.StringField(max_length=200)
    description = fields.StringField(max_length=500)
    discogs_name = fields.StringField(max_length=200)
    myspace_name = fields.StringField(max_length=200)
    website = fields.URLField(max_length=200)
    website_title = fields.StringField(max_length=200)
    # not stored: online | online status (boolean)
    track_count = fields.IntField()
    playlist_count = fields.IntField()
    followers_count = fields.LongField()
    followings_count = fields.LongField()
    public_favorites_count = fields.LongField()
    # not stored: avatar_data | binary data of user avatar

    # Subresources
    # tracks = fields.ListField(fields.ReferenceField(Track))


class Track(me.Document):
    track_id = fields.LongField(require=True)
    created_at = fields.DateTimeField()
    user_id = fields.ReferenceField(Artist)
    title = fields.StringField()
    permalink = fields.URLField(max_length=200)
    uri = fields.URLField(max_length=200)
    sharing = fields.StringField(max_length=200)
    embeddable_by = fields.StringField(max_length=200)
    purchase_url = fields.URLField(max_length=200)
    artwork_url = fields.URLField(max_length=200)
    description = fields.StringField(max_length=200)
    label = fields.ReferenceField(Artist)  #?
    duration = fields.IntField()
    genre = fields.StringField()
    tag_list = fields.ListField()
    label_id = fields.LongField()  # probably redundant
    label_name = fields.StringField()  # probably redundant
    release_number = fields.IntField()
    release_day = fields.IntField()
    release_month = fields.IntField()
    release_year = fields.IntField()
    streamable = fields.BooleanField()
    downloadable = fields.BooleanField()
    encoding_state = fields.StringField()  # either processing, failed, or finished
    license = fields.StringField()
    track_type = fields.StringField()
    # not stored: waveform url (url to png)
    download_url = fields.URLField()
    stream_url = fields.URLField()
    video_url = fields.URLField()
    bpm = fields.IntField()
    commentable = fields.BooleanField()
    isrc = fields.StringField()
    key_signature = fields.StringField()
    comment_count = fields.LongField()
    download_count = fields.LongField()
    playback_count = fields.LongField()
    favoritings_count = fields.LongField()
    # not stored: original format (file format of track)
    # not stored: original content size
    # not stored: created_with (app the track was created with)
    # not stored: asset_data (binary data of audio file)
    # not stored: artwork_data (binary data of artwork image)
    # not stored: user_favorite (track favorite of current user (boolean, authenticated requests only))

    # Subresources
    # comments
    # favoriters
    # secret-token ?

# class Playlist(models.Model):
#     # many to many with tracks
#     pass


# class Comments(models.Model):
#     pass


# class Groups(models.Model):
#     # has many artists
#     # has many Tracks
#     pass

# class 