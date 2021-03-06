# UK Political Parties

Django app and helpers for dealing with UK political parties.


## Quick start

1. Add "uk_political_parties" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'uk_political_parties',
    )

2. Run `python manage.py migrate` to create the polls models.


## How it works

This app uses the data provided by the OpenElectoralCommission project (openelectoralcommission.org.uk).  The data format for a party looks like:

    {
        "fielding_in": [], 
        "other_officers": [
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Robert Ashman", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Hayward Burt", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Simon James Vernon Eardley", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Neville Lishman", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Mark McInnes", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Michael Nicholls", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Carys Parry", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Roger Allan Pratt", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Mark Corson Roberts", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Ian Richard Sanderson", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }, 
            {
                "deputy_additional_officer": false, 
                "deputy_nominating_officer": false, 
                "name": "Julian Walden", 
                "deputy_campaigns_officer": false, 
                "deputy_treasurer": true
            }
        ], 
        "campaigns_officer": "None", 
        "registered_date": "1999-01-14T00:00:00", 
        "postcode": "SW1H 9HQ", 
        "party_leader": "The Rt Hon David Cameron", 
        "nominating_officer": "Mr Alan Mabbutt", 
        "emblems": [
            {
                "image": "raw_data/PP52/Emblem_47.gif", 
                "id": "47", 
                "description": "Emblem 1 Conservatives Emblem"
            }, 
            {
                "image": "raw_data/PP52/Emblem_48.jpg", 
                "id": "48", 
                "description": "Emblem 2 Scottish Emblem"
            }, 
            {
                "image": "raw_data/PP52/Emblem_49.gif", 
                "id": "49", 
                "description": "Emblem 3 Welsh Emblem"
            }
        ], 
        "party_address": "4 Matthew Parker Street\r\nLondon\r\nSW1H 9HQ\r\nUnited Kingdom\r\n", 
        "email": "", 
        "gibraltar_party": false, 
        "financial_year_end": "31/12", 
        "status": "Authorised", 
        "fax": "", 
        "end_date": null, 
        "phone_extension": "", 
        "phone": "", 
        "treasurer": "Mr Simon Charles Day", 
        "party_id": "PP52", 
        "accounting_units": {
            "exempt_from_parliamentary_election_returns": false, 
            "exempt_from_quarterly_transaction_returns": false, 
            "exempt_from_quarterly_donation_returns": false
        }, 
        "geometry": {
            "type": "Point", 
            "coordinates": [
                -0.13631454903857013, 
                51.49923466347958
            ]
        }, 
        "register": "Great Britain", 
        "party_name": "Conservative Party", 
        "alternative_names": [
            "Plaid Geidwadol Cymru"
        ], 
        "descriptions": [
            {
                "translation": "", 
                "description": "For real change in Europe"
            }, 
            {
                "translation": "", 
                "description": "Scottish Conservative and Unionist"
            }, 
            {
                "translation": "", 
                "description": "Scottish Conservatives Vote No to Independence"
            }, 
            {
                "translation": "", 
                "description": "Local Conservatives"
            }, 
            {
                "translation": "", 
                "description": "David Cameron's Conservatives"
            }, 
            {
                "translation": "Welsh Conservatives", 
                "description": "Ceidwadwyr Cymreig"
            }, 
            {
                "translation": "", 
                "description": "Conservatives: Vote blue, go green"
            }, 
            {
                "translation": "", 
                "description": "Conservatives: Stop the hospital cuts"
            }, 
            {
                "translation": "", 
                "description": "The Conservative Party Candidate"
            }, 
            {
                "translation": "", 
                "description": "Conservative Party Candidate"
            }, 
            {
                "translation": "Ymgeisydd Plaid Geidwadol Cymru", 
                "description": "Welsh Conservative Party Candidate"
            }, 
            {
                "translation": "", 
                "description": "Conservative and Unionist Party"
            }
        ]
    }, 