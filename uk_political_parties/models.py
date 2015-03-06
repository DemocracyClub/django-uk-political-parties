# -*- coding: utf-8 -*-
import datetime
import re

from django.db import models
from django_extensions.db.fields import  AutoSlugField


class PartyManger(models.Manager):

    def _alternative_name_guesses(self, name):
        """
        Returns a list of names to try, including removing common errors
        and different ways of spelling them (i.e., removing 'The' form the
        start of the name)
        """
        return [
            name,
            re.sub(r"([^\[]+)\[The\]", r"The \1", name).strip(),
            re.sub(r"([^\[]+)\[The\]", r"\1", name).strip(),
            re.sub(r"^The(.*)", r"\1", name).strip(),
            re.sub(r"\([^\)]+\)", r"", name).strip(),
            re.sub(r"United Kingdom", r"UK", name).strip(),
        ]

    def _clean_known_names(self, name):
        if name == "Animals Count":
            return "Animal Welfare Party"
        if name == "Independent Community and Health Concern":
            return "Independent Kidderminster Hospital and Health Concern"
        if name == "United Kingdom Independence Party":
            return "UK Independence Party (UK I P)"
        if name == "Independent or Independent Network":
            return "Independent"
        if name == u"National Liberal Party, Third Way":
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
        if name == "Scottish National Party":
            return "Scottish National Party (SNP)"
        if name == "Sinn Fein":
            return "Sinn Féin"
        if name == "Yes to AV":
            return "Yes in May 2011 Ltd"
        return name

    def _match_name(self, name, party_type, register):
        # import ipdb; ipdb.set_trace()
        matches = self.filter(
            party_name__iexact=name,
            party_type=party_type,
            register=register
            ).order_by('-weight')
        if matches:
            return matches[0]


    def find_party_by_name(self, name):
        """
        Given a name, try to match to a party, using increasingly
        hacky methods.

        Returns the first party found with a reasonably similar name.

        Searches from large UK wide parties to small parties, and picks active
        parties over deregistered ones.
        """
        name = self._clean_known_names(name)
        if name.lower().strip() in ["unknown party",
                    "other",
                    "independent",
                    "the speaker seeking re-election",
                    "no to av",
                ]:
            return None

        party_search_order = [
            "Political Party",
            "Minor Party",
            "Permitted Participant",
            "Third Party",
        ]

        register_search_order = [
            "Great Britain",
            "Northern Ireland",
            None
        ]

        names = self._alternative_name_guesses(name)
        match = None
        for register in register_search_order:
            for party_type in party_search_order:
                for name in names:
                    match = self._match_name(name, party_type, register)
                    if match:
                        return match
        if not match:
            raise ValueError


class PartyEmblem(models.Model):
    party = models.ForeignKey('Party', related_name='emblems')
    emblem_url = models.URLField(blank=True)

    class Meta:
        ordering = ('emblem_url', )


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
    weight = models.IntegerField(blank=True, null=True)

    objects = PartyManger()

    class Meta:
        verbose_name_plural = 'Parties'
        ordering = ('-weight', 'party_name', )

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
