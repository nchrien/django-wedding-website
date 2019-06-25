from django.conf.urls import url

from guests.views import rsvp

urlpatterns = [
    url(r'^rsvp/$', rsvp, name='rsvp'),
]
