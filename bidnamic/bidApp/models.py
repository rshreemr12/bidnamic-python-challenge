from django.db import models

# Create your models here.

class Campaigns(models.Model):
    STATUS_CHOICE = [('E', 'ENABLED'), ('R', 'REMOVED')]
    structure_value = models.CharField(max_length=10)
    status = models.CharField(max_length=1,choices=STATUS_CHOICE)
    campaign_id = models.IntegerField(primary_key=True)



class AdGroups(models.Model):
    STATUS_CHOICE = [('E', 'ENABLED'), ('R', 'REMOVED')]
    status = models.CharField(max_length=1,choices=STATUS_CHOICE)

    alias = models.CharField(max_length=30)
    ad_group_id = models.IntegerField(primary_key=True)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)



class SearchTerm(models.Model):
    ad_group = models.ForeignKey(AdGroups, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)
    clicks = models.IntegerField()
    cost = models.FloatField()
    conversion_value = models.FloatField()
    conversions = models.IntegerField()
    search_term = models.TextField()
    date = models.DateField()

    roas = models.FloatField()


