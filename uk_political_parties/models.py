# -*- coding: utf-8 -*-
import datetime
import re

from django.db import models
from django_extensions.db.fields import  AutoSlugField

class PartyManger(models.Manager):

    def find_party_by_name(self, name):
        """
        Given a name, try to match to a party, using increasingly hacky methods.

        Returns the first party found with a reasonably similar name.

        Searches from large UK wide parties to small parties, and picks active
        parties over deregistered ones.
        """

        def _match_name(name):
            # name = name.lower()
            matches = self.filter(party_name__iexact=name)
            if matches:
                if len(matches) > 1:
                    matches = matches.filter(party_type='Political Party')
                    if len(matches) > 1:
                        matches = matches.filter(register='Great Britain')
                        if len(matches) > 1:
                            matches = matches.filter(status='Authorised')
                            if len(matches) > 1:
                                print matches
                if len(matches) == 1:
                    return matches[0]
                else:
                    print "ERROR More than one match, ", matches

            matches = self.filter(party_name__istartswith=name)
            if matches:
                name = matches[0].party_name
                match = _match_name(name)
                if match:
                    return match
            if len(matches) == 1:
                return matches[0]

            matches = self.filter(party_name__contains=name)
            if matches:
                match = _match_name(matches[0].party_name)
                if match:
                    return match

        def _clean_known_names(name):
            if name == "Animals Count":
                return "Animal Welfare Party"
            if name == "Independent Community and Health Concern":
                return "Independent Kidderminster Hospital and Health Concern"
            if name == "Independent or Independent Network":
                return "Independent"
            if name == u"National Liberal Party, Third Way":
                print "FOUND"
                return "Ulster Third Way"
            if name == u"National Liberal Party, The Third Way":
                return "Ulster Third Way"
            if name == "Plaid Cymru - Party of Wales":
                return "Plaid Cymru - The Party of Wales"
            if name == "Plaid Cymru - Party of Wales [The]":
                return "Plaid Cymru - The Party of Wales"
            if name == "Trade Unionist and SocialistCoalition":
                return "Trade Unionist and Socialist Coalition"
            if name == "WAI D":
                return "Your Decision"
            if name == "Movement for Active Democracy! (M.A.D!)":
                return "Movement for Active Democracy (M.A.D.)"
            if name == "Sinn Fein":
                return "Sinn Féin"
            if name == "Yes to AV":
                return "Yes in May 2011 Ltd"
            return name

        name = _clean_known_names(name)
        match = _match_name(name)
        if not match:
            old_name = name
            name = re.sub(r"([^\[]+)\[The\]", r"The \1", name).strip()
            match = _match_name(name)
            if not match:
                name = re.sub(r"^The(.*)", r"\1", name).strip()
                match = _match_name(name)
        if match:
            return match


class PartyEmblem(models.Model):
    party = models.ForeignKey('Party', related_name='emblems')
    emblem_url = models.URLField(blank=True)


class Party(models.Model):
    """
    Represents a UK political party.
    """
    party_id = models.CharField(blank=True, max_length=100, primary_key=True)
    party_name = models.CharField(max_length=765)
    registered_date = models.DateField(default=datetime.datetime.today)
    party_address = models.TextField(blank=True)
    postcode = models.CharField(blank=True, max_length=15, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=100)
    slug = AutoSlugField(populate_from='party_name')
    party_type = models.CharField(blank=True, max_length=100)
    register = models.CharField(max_length=255,
        help_text="Country the party is registered in", null=True, blank=True)

    objects = PartyManger()

    class Meta:
        verbose_name_plural = 'Parties'
        ordering = ('party_name', )

    def save(self, *args, **kwargs):
        if self.party_id.startswith('TP'):
            self.party_type = "Third Party"
        if self.party_id.startswith('PerPar'):
            self.party_type = "Permitted Participant"
        if self.party_id.startswith('PP'):
            self.party_type = "Political Party"
        if self.party_id.startswith('PPm'):
            self.party_type = "Minor Party"

        super(Party, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s (%s)" % (self.party_name, self.pk)


