"""bidnamic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from bidApp import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'campaigns', views.CampaignsViewSet)
router.register(r'adgroups', views.AdGroupsViewSet)
router.register(r'search_term', views.SearchTermViewSet)

# further routing
router.register('campaigns/<int:campaign_id/>', views.CampaignsViewSet) 
# router.register((r'^my-own-view/$', views.QueryViewSet())),


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# UUID_CHANNEL_REGEX = r'channel/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'


urlpatterns = [
    path('admin/', admin.site.urls) ,
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('query/<str:pk_test>/<str:pk_test1>', views.query_top_10, name="query"),

    # path('query/<str:slug>/<str:slug1>', views.query_top_10, name="query"),
    # re_path(r'channel/(?P<slug>[\w-]+)/(?P<slug2>[\w-]+)/$', views.dec_up),

    # re_path(r'^/blog/(?P<slug>[\w-]+)/(?P<slug2>[\w-]+)/$', views.dec_up, name="multiple_slug_regex"),
    # path.url(r'^some_url/$', dispatch(get=views.dec_up), name='events_json'),

]   