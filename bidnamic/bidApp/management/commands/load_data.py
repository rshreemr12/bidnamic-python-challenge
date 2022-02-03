from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from bidApp.models import Campaigns, AdGroups, SearchTerm
from pytz import UTC


DATETIME_FORMAT = '%Y-%m-%d' #'%m/%d/%Y'

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
        
        if Campaigns.objects.exists(): 
            print('Data Campaigns already loaded...exiting!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            
        else :
            print("Loading campaigns Data !")
            for row in DictReader(open(r'E:\bidnamic_\data\campaigns.csv')):
                ci = Campaigns()
                ci.campaign_id = row['campaign_id']
                ci.structure_value = row['structure_value']
                ci.status = row['status']
                ci.save()
        
        if  AdGroups.objects.exists():
            print('Data AdGroups already loaded...exiting!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            # return
        else:
            print("Loading adgroups Data !")

            for row in DictReader(open(r'E:\bidnamic_\data\adgroups.csv')):
                ag = AdGroups()
                ag.alias = row['alias']
                ag.ad_group_id = row['ad_group_id']
                ag.status = row['status']

                print(f"\n\n campaign_id: {row['campaign_id']}  \n\n\n")
                print(f"\n\n  {Campaigns.objects.filter(campaign_id = row['campaign_id']).first().campaign_id } \n\n\n")

                ci = Campaigns.objects.filter(campaign_id = row['campaign_id']).first()
                ag.campaign = ci

                ag.save()

        if  SearchTerm.objects.exists():
            print('Data SearchTerm already loaded...exiting!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        else:
            print("Loading search_terms Data !")
            
            for row in DictReader(open(r'E:\bidnamic_\data\search_terms_1.csv')):
                obj = SearchTerm()
                # obj.ad_group_id = row['ad_group_id']
                # obj.Campaign_id = row['Campaign_id']
                obj.id = row['id']
                obj.clicks = row['clicks']
                obj.cost = row['cost']
                obj.conversion_value = row['conversion_value']
                obj.conversions = row['conversions']
                obj.search_term = row['search_term']
                obj.roas = row['roas']
                raw_submission_date = row['date']
                date = UTC.localize(
                    datetime.strptime(raw_submission_date, DATETIME_FORMAT))
                obj.date = date


                ci = Campaigns.objects.filter(campaign_id = row['campaign_id']).first()
                obj.campaign = ci
                
                ag = AdGroups.objects.filter(ad_group_id = row['ad_group_id']).first()
                obj.ad_group = ag
                
                print(f"\n\n campaign_id: {row['campaign_id']}  \n\n\n")

                obj.save()
    
