from django.contrib import admin

from .models import Campaigns, AdGroups, SearchTerm
# Register  models here.

# adding capability for admin to perform CRUD operations 


@admin.register(Campaigns)
class CampaignsDisplay(admin.ModelAdmin):
    list_display = ['campaign_id', 'structure_value'] # ,'status']

@admin.register(AdGroups)
class CampaignsDisplay(admin.ModelAdmin):
    list_display = ['campaign_id', 'ad_group_id', 'alias'] # ,'status']


@admin.register(SearchTerm)
class SearchTermval(admin.ModelAdmin):
    list_display = ['date', 'ad_group_id', 'campaign_id','conversion_value', 'search_term']
