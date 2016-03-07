"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Employee


def index(request):
    employee = Employee.objects.create(
        email="example@company.com",
        first_name="lol",
        last_name="haha"
    )
    employee.save()
    print(Employee.objects.all())
    return render(request, 'app/index.html')
