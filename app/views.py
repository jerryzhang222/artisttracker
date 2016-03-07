"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Artist, Track


def index(request):
    artist = Artist.objects.create(
        soundcloud_id=1234
    )
    artist.save()
    print(Artist.objects.all())
    return render(request, 'app/index.html')
