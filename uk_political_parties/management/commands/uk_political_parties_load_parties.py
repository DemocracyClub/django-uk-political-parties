from urllib2 import urlopen
import json

from django.core.management.base import BaseCommand

from uk_political_parties.models import Party, PartyEmblem


class Command(BaseCommand):
    def fetch_parties(self):
        base_url = "http://openelectoralcommission.org.uk"
        req = urlopen(base_url + '/parties/index.json')
        return json.loads(req.read())

    def clean_party(self, party):
        """
        Takes the raw dict from OpenElectoralCommission and returns a dict
        that's able to be used by the django model.  This is needed because
        this app doesn't support the full JSON provided yet.
        """

        cleaned_party = {
            'party_id': party['party_id'],
            'party_name': party['party_name'],
            'registered_date': party['registered_date'].split('T')[0],
            'party_address': party['party_address'],
            'postcode': party.get('postcode'),
            'email': party['email'],
            'status': party['status'],
            'register': party['register'],
        }
        return cleaned_party

    def handle(self, **options):
        parties = self.fetch_parties()
        for party in parties:
            Party.objects.update_or_create(
                party_id=party['party_id'],
                defaults=self.clean_party(party))
            if party['emblems']:
                for emblem in party['emblems']:
                    PartyEmblem.objects.update_or_create(
                        party_id=party['party_id'],
                        defaults={'emblem_url': emblem['image']})
