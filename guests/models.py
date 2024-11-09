from __future__ import unicode_literals
import datetime
import uuid
import string
import random

from django.db import models
from django.dispatch import receiver


DEFAULT_DIETS = [
    "Vegetarisch",
    "Vegan",
    "Fleisch",
    "Fisch",
]

DEFAULT_DRINKS = [
    "Unalkoholisch",
    "Bier",
    "Weißwein",
    "Rotwein",
    "Harter Alk",
]


def _random_id():
    chars = string.digits + string.ascii_letters + "$-_+!*"
    random_id = ''
    loop = True
    while loop:
        random_id = ''.join(random.choice(chars) for i in range(8))
        qs = Party.objects.filter(invitation_id=random_id)
        loop = qs.exists()
    return random_id


class Party(models.Model):
    """
    A party consists of one or more guests.
    """
    name = models.CharField(max_length=128)
    save_the_date_sent = models.DateField(null=True, blank=True, default=None)
    invitation_id = models.CharField(max_length=32, db_index=True, default=_random_id, unique=True)
    invitation_sent = models.DateField(null=True, blank=True, default=None)
    invitation_opened = models.DateTimeField(null=True, blank=True, default=None)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Gruppe: {}'.format(self.name)

    @property
    def any_guests_attending_wedding(self):
        return any(self.guest_set.values_list('is_attending_wedding', flat=True))
    
    @property
    def any_guests_attending_brunch(self):
        return any(self.guest_set.values_list('is_attending_brunch', flat=True))

    @property
    def guest_emails(self):
        return list(filter(None, self.guest_set.values_list('email', flat=True)))


class BringAlongMeal(models.Model):
    """
    A meal that a party brings along to the wedding.
    """
    parties = models.ManyToManyField(Party, blank=True)
    type = models.CharField(max_length=128)
    max_number = models.IntegerField()

    def __str__(self):
        return 'Essen: {}'.format(self.type)
    
    @property
    def assigned(self):
        return len(self.parties.all())
    
    @property
    def no_more_needed(self):
        return self.assigned >= self.max_number
    
    @property
    def still_needed(self):
        return not self.no_more_needed


class DietOption(models.Model):
    """
    The preferred diet of a guest.
    """
    type = models.CharField(max_length=128)

    def __str__(self):
        return 'Diet: {}'.format(self.type)
    

class DrinkOption(models.Model):
    """
    The preferred drinks of a guest.
    """
    type = models.CharField(max_length=128)

    def __str__(self):
        return 'Drink: {}'.format(self.type)
    

class Guest(models.Model):
    """
    A single guest
    """
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, null=True, blank=True)
    is_attending_wedding = models.BooleanField(default=None, null=True)
    is_attending_brunch = models.BooleanField(default=None, null=True)
    diets = models.ManyToManyField(DietOption, blank=True)
    drinks = models.ManyToManyField(DrinkOption, blank=True)

    @property
    def unique_id(self):
        # convert to string so it can be used in the "add" templatetag
        return str(self.pk)

    def __str__(self):
        return 'Gast: {}'.format(self.name)

