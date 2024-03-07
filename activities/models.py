from django.db import models

class Activity(models.Model):
    activity = models.CharField(max_length=150, blank=False, null=False)
    starting_date = models.DateField()
    starting_time = models.TimeField()
    ending_date = models.DateField()
    ending_time = models.TimeField()

    busy_or_free = models.CharField(max_length=150, blank=True, null=True, default="Busy")
    notes = models.TextField()

    user_responsible = models.CharField(max_length=150, blank=False, null=False)
    deal_or_lead = models.CharField(max_length=150, blank=False, null=False)
    people = models.CharField(max_length=250, blank=False, null=False)
    organization = models.CharField(max_length=150, blank=False, null=False)

