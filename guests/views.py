from django.shortcuts import render

def rsvp(request):
    return render(request, 'guests/rsvp.html', {})