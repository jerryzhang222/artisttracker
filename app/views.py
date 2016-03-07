"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Artist, Track


def index(request):
    employee = Employee.objects.create(
        email="example@company.com",
        first_name="lol",
        last_name="haha"
    )
    employee.save()
    artist = Artist.objects.create(
        soundcloud_id=1234
    )
    artist.save()
    print(Artist.objects.all())
    return render(request, 'app/index.html')
