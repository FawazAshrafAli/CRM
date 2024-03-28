from django.db import models
from authentication.models import CrmUser

class Company(models.Model):
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)
    # Organization Name
    name = models.CharField(max_length=250, blank=False, null=False)
    organization = models.CharField(max_length=150, blank=False, null=False)    
    title = models.CharField(max_length=150, blank=False, null=False)

    # Organization Contact Details
    phone = models.CharField(max_length=25, blank=False, null=False)
    fax = models.CharField(max_length=25, blank=False, null=False)
    website = models.CharField(max_length=150, blank=False, null=False)
    linkedin = models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    email_domains = models.CharField(max_length=250, blank=False, null=False)

    # Address Information
    billing_address = models.TextField()    
    billing_city = models.CharField(max_length=150, blank=False, null=False)    
    billing_state = models.CharField(max_length=150, blank=False, null=False)
    billing_postal_code = models.CharField(max_length=25, blank=False, null=False)
    billing_country = models.CharField(max_length=150, blank=False, null=False)

    shipping_address = models.TextField(blank=True, null=True)
    shipping_city = models.CharField(max_length=150, blank=True, null=True)
    shipping_state = models.CharField(max_length=150, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=25, blank=True, null=True)
    shipping_country = models.CharField(max_length=150, blank=True, null=True)

    # Additional Information
    date_to_remember = models.CharField(max_length=150, blank=True, null=True)

    # Description Information
    description = models.TextField(blank=True, null=True)

    # Tag Information
    tag_list = models.CharField(max_length=250, blank=True, null=True)

    # Permissions
    permission = models.CharField(max_length=150, blank=True, null=True)

    # Record Owner
    record_owner = models.ForeignKey(CrmUser, on_delete=models.CASCADE, blank=True, null=True)

    # Created and Updated Datetimes
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
