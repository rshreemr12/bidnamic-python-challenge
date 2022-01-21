from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from bidApp.models import Campaigns, AdGroups, SearchTerm
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y'

# VACCINES_NAMES = [
#     'Canine Parvo',
#     'Canine Distemper',
#     'Canine Rabies',
#     'Canine Leptospira',
#     'Feline Herpes Virus 1',
#     'Feline Rabies',
#     'Feline Leukemia'
# ]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the  data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

files_to_load = ['search_terms.csv','campaigns.csv','adgroups.csv']

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from CSV files"

    def handle(self, *args, **options):
        if Campaigns.objects.exists() or AdGroups.objects.exists() or SearchTerm.objects.exists():
            print('Data already loaded...exiting!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        # print("Creating Campaigns data")
        # for vaccine_name in VACCINES_NAMES:
        #     vac = Vaccine(name=vaccine_name)
        #     vac.save()
        print("Loading SearchTerm Data !")

        for row in DictReader(open(r'E:\bidnamic_\data\campaigns.csv')):
            ci = Campaigns()
            ci.campaign_id = row['campaign_id']
            ci.structure_value = row['structure_value']
            ci.status = row['status']
            ci.save()

        for row in DictReader(open(r'E:\bidnamic_\data\adgroups.csv')):
            ag = AdGroups()
            ag.alias = row['alias']
            ag.ad_group_id = row['ad_group_id']
            ag.status = row['status']
            # ci.campaign_id = row['campaign_id']

            ci = Campaigns.objects.get(row['campaign_id'])
            ag.campaign_id.add(ci)
            ag.save()


        for row in DictReader(open(r'E:\bidnamic_\data\search_terms.csv')):
            obj = SearchTerm()
            # obj.ad_group_id = row['ad_group_id']
            # obj.Campaign_id = row['Campaign_id']
            obj.clicks = row['clicks']
            obj.cost = row['cost']
            obj.conversion_value = row['conversion_value']
            obj.conversions = row['conversions']
            obj.search_term = row['search_term']
            raw_submission_date = row['date']
            date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            obj.submission_date = date


            ci = Campaigns.objects.get(row['campaign_id'])
            obj.campaign_id.add(ci)

            ag = Campaigns.objects.get(row['ad_group_id'])
            obj.campaign_id.add(ag)

            obj.save()
            # raw_vaccination_names = row['vaccinations']
            # vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            # for vac_name in vaccination_names:
            #     vac = Vaccine.objects.get(name=vac_name)
            #     pet.vaccination.add(vac)
            # pet.save()

