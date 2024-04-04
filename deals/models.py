from django.db import models
from organizations.models import Company
from authentication.models import CrmUser

class PipelineStage(models.Model):
    stage = models.CharField(max_length=150)

    def __str__(self):
        return self.stage

class Deal(models.Model):
    image = models.ImageField(upload_to='deal_images/', blank=True, null=True)

    prefix = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=True, null=True)    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)

    # Additional Informations
    email = models.EmailField(max_length=254, blank=False, null=False)
    email_opted_out = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    industry = models.CharField(max_length=150, blank=True, null=True)
    number_of_employees = models.CharField(max_length=50, blank=True, null=True)

    category = models.CharField(max_length=150, blank=True, null=True, default="Email")
    probability_of_winning = models.CharField(max_length=150, blank=True, null=True, default="Email")
    forecast_close_date = models.CharField(max_length=150, blank=True, null=True)
    actual_close_date = models.CharField(max_length=150, blank=True, null=True)
    user_responsible = models.ForeignKey(CrmUser, on_delete=models.PROTECT, blank=True, null=True)
    deal_value = models.CharField(max_length=100, blank=True, null=True)
    bid_amount = models.CharField(max_length=50, blank=True, null=True)
    bid_type = models.CharField(max_length=100, blank=True, null=True, default="Fixed Bid")

    # Address Information
    mailing_address = models.TextField(blank=False, null=False)
    mailing_city = models.CharField(max_length=50, blank=False, null=False)
    mailing_state = models.CharField(max_length=50, blank=False, null=False)
    mailing_postal_code = models.CharField(max_length=15, blank=False, null=False)
    mailing_country = models.CharField(max_length=100, blank=False, null=False)

    # Description Information
    description = models.TextField(blank=True, null=True)

    # Tag Information
    tag_list = models.CharField(max_length=150, blank=True, null=True)

    # Pipeline and Stages
    pipeline = models.CharField(max_length=150, blank=True, null=True)    
    stage = models.ManyToManyField(PipelineStage)

    # Permissions
    visibility = models.CharField(max_length=150, blank=True, null=True)

    record_owner = models.ForeignKey(CrmUser, blank=True, null=True, on_delete=models.CASCADE, related_name="record_owner")
    
    # Created and Updated Datetime
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name