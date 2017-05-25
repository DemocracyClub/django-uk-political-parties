import requests

from django.core.management.base import BaseCommand

from uk_political_parties.models import Party, PartyEmblem


class Command(BaseCommand):

    def clean_party(self, party_id, party):
        """
        Takes the raw dict from OpenElectoralCommission and returns a dict
        that's able to be used by the django model.  This is needed because
        this app doesn't support the full JSON provided yet.
        """

        cleaned_party = {
            'party_id': party_id,
            'party_name': party['name'],
            'registered_date': party['founding_date'],
            'register': party['party_sets'][0]['slug'],
        }
        return cleaned_party

    def handle(self, **options):
        print("workng")

        base_url = "https://candidates.democracyclub.org.uk"
        url = "{}/api/v0.9/organizations/".format(base_url)

        while url:
            req = requests.get(url)
            results = req.json()
            organizations = results['results']
            for org in organizations:
                if org['classification'] != "Party":
                    continue

                party_id = [
                    i['identifier'] for i in org['identifiers']
                    if i['scheme'] == "electoral-commission"
                ]
                if party_id:
                    party_id = party_id[0]
                else:
                    continue
                (party_obj, cerated) = Party.objects.update_or_create(
                    party_id=party_id,
                    defaults=self.clean_party(party_id, org))

                if org['images']:
                    for emblem in org['images']:
                        PartyEmblem.objects.update_or_create(
                            party_id=party_id,
                            emblem_url=emblem['image_url'],
                        )
            url = results.get('next', None)
