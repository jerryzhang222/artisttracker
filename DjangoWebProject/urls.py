"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url, include
from app.forms import BootstrapAuthenticationForm

urlpatterns = [
    # Examples:
    url(r'^', include('app.urls')), # app will occupy the root path urls
]