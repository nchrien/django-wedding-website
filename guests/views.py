from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.forms import inlineformset_factory

from .forms import PartyForm
from .models import Party, Guest

def rsvp(request):
    GuestFormSet = inlineformset_factory(Party, Guest, fields = ('first_name', 'last_name', 'is_attending', 'is_attending_luncheon', 'dietary_restrictions', 'dietary_restriction_details', 'child_meal'))
    party = Party()

    if request.method == 'POST':
        partyForm = PartyForm()
        formset = GuestFormSet(instance = party)
        
        partyForm = PartyForm(request.POST)
        if partyForm.is_valid():
            newParty = partyForm.save()
            
            formset = GuestFormSet(request.POST, instance = newParty)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect('/rsvp/confirmation/')

    else:
        formset = GuestFormSet(instance = party)
        partyForm = PartyForm()

    return render(request, 'guests/rsvp.html', {'form': partyForm, 'formset': formset})


def rsvpConfirmation(request):
    return HttpResponse("Thank you for RSVPing!")