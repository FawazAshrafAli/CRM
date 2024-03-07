from django.db import models

class Deal(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    company = models.CharField(max_length=150, blank=False, null=False)

    # Additional Informations
    category = models.CharField(max_length=150, blank=True, null=True, default="Email")
    probability_of_winning = models.CharField(max_length=150, blank=True, null=True, default="Email")
    forecast_close_date = models.DateField()
    actual_close_date = models.DateField()
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
    stage = models.CharField(max_length=150, blank=False, null=False)

    # Permissions
    visibility = models.CharField(max_length=150, blank=False, null=False)
    
    # Created and Updated Datetime
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)