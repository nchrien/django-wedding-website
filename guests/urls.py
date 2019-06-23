from django.conf.urls import url

from guests.views import rsvp # GuestListView, test_email, save_the_date_preview, save_the_date_random, export_guests, \
    # invitation, invitation_email_preview, invitation_email_test, rsvp_confirm, dashboard

urlpatterns = [
    url(r'^rsvp/$', rsvp, name='rsvp'),
]
