from django.test import TestCase
from datetime import datetime


from .models import SearchTerm, AdGroups, Campaigns
from bidApp import views


"""

"""

class test_Campaigns(TestCase):
    ci = Campaigns.objects.filter(structure_value =  "")
    expected_cam_id = 123
    actual_id = 1578411800
    assert (expected_cam_id == actual_id)



class SearchTermsTestCase(TestCase):

    def test_roas_calculated_on_initilization_ok(self):
        st = SearchTerm(
            date = datetime.now(),
            ad_group = AdGroups(ad_group_id=100),
            campaign = Campaigns(campaign_id=100),
            clicks = 1,
            cost = 0.11,
            conversion_value = 0.5,
            conversions = 1,
            search_term = "Linus drop tips",
        )
        expected = 0.5 / 0.11
        actual = st.roas
        assert expected == actual, f'Expected: {expected} got: {actual}'

    def test_roas_calculated_on_save_division_by_zero_ok(self):
        st = SearchTerm(
            date = datetime.now(),
            ad_group = AdGroups(ad_group_id=100),
            campaign = Campaigns(campaign_id=100),
            clicks = 1,
            cost = 0,
            conversion_value = 0.5,
            conversions = 1,
            search_term = "Linus drop tips",
        )
        expected = 0
        actual = st.roas
        assert expected == actual, f'Expected: {expected} got: {actual}'

        
