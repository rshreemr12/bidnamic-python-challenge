from django.shortcuts import render, HttpResponse
from django.http import Http404,JsonResponse
from django.contrib.auth.models import User, Group


from rest_framework import viewsets,permissions, filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from bidApp.serializers import UserSerializer, GroupSerializer, CampaignSerializer,  AdgroupSerializer, \
SearchTermSerializer, QuestionSerializer

from bidApp.models import Campaigns, AdGroups, SearchTerm

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CampaignsViewSet(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


class CampaignsViewSet_id(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all() 
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdGroupsViewSet(viewsets.ModelViewSet):
    queryset = AdGroups.objects.all() 
    serializer_class = AdgroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SearchTermViewSet(viewsets.ModelViewSet):
    queryset = SearchTerm.objects.all() 
    serializer_class = SearchTermSerializer
    permission_classes = [permissions.IsAuthenticated]

def dec_up(request, slug, slug2):
    print(f"\n\n\n {slug, slug2} \n\n\n")



@api_view(['GET','PUT', 'DELETE'])
def query_top_10(request, pk_test, pk_test1):

    print("pktest: ", pk_test)
    print("pktest1: ", pk_test1)

    try:
        searches = []
    
        # would execute with ads None , cams not none 
        if pk_test!="" :
            cams = Campaigns.objects.filter(structure_value=pk_test).values('structure_value', 'campaign_id')

            for cam in list(cams):
                #  ad_group, ad_group_id, campaign, campaign_id, clicks, conversion_value, conversions, cost, date, id, search_term
                search_obj = SearchTerm.objects.filter(campaign_id=cam.get('campaign_id')).values('ad_group_id', 'campaign_id', 
                'conversion_value','clicks','cost','search_term','date', 'conversions', 'roas')
                
                print(f"cams: {cam}, {search_obj}", end="\n\n\n\n")

                if search_obj:
                    searches.append(search_obj.all().order_by('roas'))

        if pk_test1!="" :     
            ads = AdGroups.objects.filter(alias=pk_test1).values('ad_group_id', 'campaign_id', 'alias')

            for ad in list(ads):
                #  ad_group, ad_group_id, campaign, campaign_id, clicks, conversion_value, conversions, cost, date, id, search_term
                search_obj = SearchTerm.objects.filter(campaign_id=ad.get('campaign_id')).values('ad_group_id', 'campaign_id', 
                'conversion_value','clicks','cost','search_term','date', 'conversions', 'roas')
                
                if search_obj:
                    searches.append(search_obj.all().order_by('roas'))
                    # searches.append(json.dumps(str(search_obj)))
                    # return JsonResponse(searches, safe=False)
                    # return HttpResponse(searches)

        if searches:
            return  Response(searches)
        else:
            return HttpResponse("<p> No Match found! </p>")

    except Campaigns.DoesNotExist or AdGroups.DoesNotExist or Exception:
        return HttpResponse(Http404)

    # return render(request, 'appfolder/show.html', {'post': query})
    # return HttpResponse(f"{query.ad_group_id, query.campaign_id}")


# @api_view(['GET'])
# class QuestionsAPIView():
#     search_fields = ['alias']
#     filter_backends = (filters.SearchFilter,)
#     queryset = AdGroups.objects.all()
#     serializer_class = QuestionSerializer