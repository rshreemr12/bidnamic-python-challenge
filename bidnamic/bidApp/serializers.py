from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Campaigns, AdGroups, SearchTerm

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaigns
        fields = ['campaign_id', 'structure_value' , 'status']


class AdgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdGroups
        fields = ['campaign_id', 'ad_group_id', 'alias' ,'status']

class SearchTermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchTerm
        fields = ['campaign_id', 'ad_group_id', 'cost', 'clicks', 'conversion_value', 'conversions', 'search_term', 'date', 'roas']




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdGroups
        fields = '__all__'