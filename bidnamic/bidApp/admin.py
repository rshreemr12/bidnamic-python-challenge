from django.contrib import admin

from .models import Campaigns, AdGroups, SearchTerm
# Register your models here.

@admin.register(SearchTerm)
class SearchTermval(admin.ModelAdmin):
    list_display = ['date', 'ad_group_id', 'Campaign_id','conversion_value', 'search_term']
