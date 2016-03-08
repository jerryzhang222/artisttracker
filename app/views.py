from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Artist, Track
import soundcloud
import pprint
from random import randint

soundcloud_client = soundcloud.Client(client_id='c892b76c132acff5771cb267a7e5a618')

def index(request):
    artist = Artist.objects.create(
        soundcloud_id=randint(0,100000)
    )
    artist.save()
    # artist = soundcloud_client.get('/users', q="skrillex")[0].__dict__
    # print(artist['obj'])
    return render(request, 'app/index.html')
