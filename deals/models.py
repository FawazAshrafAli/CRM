from django.db import models
from organizations.models import Company

class Deal(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # Additional Informations
    category = models.CharField(max_length=150, blank=True, null=True, default="Email")
    probability_of_winning = models.CharField(max_length=150, blank=True, null=True, default="Email")
    forecast_close_date = models.CharField(max_length=150, blank=True, null=True)
    actual_close_date = models.CharField(max_length=150, blank=True, null=True)
    user_responsible = models.CharField(max_length=150, blank=False, null=False)
    deal_value = models.CharField(max_length=100, blank=False, null=False)
    bid_amount = models.CharField(max_length=50, blank=False, null=False)
    bid_type = models.CharField(max_length=100, blank=False, null=False, default="Fixed Bid")

    # Description Information
    description = models.TextField()

    # Tag Information
    tag_list = models.CharField(max_length=150)

    # Pipeline and Stages
    pipeline = models.CharField(max_length=150, blank=False, null=False)
    stage = models.JSONField(blank=True, null=True)

    # Permissions
    visibility = models.CharField(max_length=150, blank=False, null=False)
    
    # Created and Updated Datetime
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)