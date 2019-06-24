from django.db import models

class Party(models.Model):
    """
    A party consists of one or more guests.
    """
    contact_email = models.EmailField(null = True, blank = True)
    comments = models.TextField(null = True, blank = True)


class DietaryRestriction(models.Model):
    name = models.CharField(max_length = 20)

    
class Guest(models.Model):
    """
    A single guest
    """
    party = models.ForeignKey(Party, on_delete = models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    is_attending = models.NullBooleanField(default = None)
    is_attending_luncheon = models.NullBooleanField(default = None)
    dietary_restrictions = models.ManyToManyField(DietaryRestriction)
    dietary_restriction_details = models.TextField(null = True, blank = True)
    child_meal = models.BooleanField(default = False)