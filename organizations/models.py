from django.db import models

class Company(models.Model):
    # Organization Name
    name = models.CharField(max_length=250, blank=False, null=False)
    organization = models.CharField(max_length=150, blank=False, null=False)
    title = models.CharField(max_length=150, blank=False, null=False)

    # Organization Contact Details
    phone = models.CharField(max_length=25, blank=False, null=False)
    fax = models.CharField(max_length=25, blank=False, null=False)
    website = models.CharField(max_length=150, blank=False, null=False)
    linkedin = models.CharField(max_length=150, blank=False, null=False)
    facebook = models.CharField(max_length=150, blank=False, null=False)
    twitter = models.CharField(max_length=150, blank=False, null=False)
    email_domains = models.CharField(max_length=250, blank=False, null=False)

    # Address Information
    billing_address = models.TextField()
    billing_street = models.CharField(max_length=150, blank=False, null=False)
    billing_city = models.CharField(max_length=150, blank=False, null=False)    
    billing_state = models.CharField(max_length=150, blank=False, null=False)
    billing_postal_code = models.CharField(max_length=25, blank=False, null=False)
    billing_country = models.CharField(max_length=150, blank=False, null=False, default="India")

    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=150, blank=False, null=False)
    shipping_state = models.CharField(max_length=150, blank=False, null=False)
    shipping_postal_code = models.CharField(max_length=25, blank=False, null=False)
    shipping_country = models.CharField(max_length=150, blank=False, null=False, default="India")

    # Additional Information
    date_to_remember = models.DateField()

    # Description Information
    description = models.TextField()

    # Tag Information
    tag_list = models.CharField(max_length=250)

    # Permissions
    permission = models.CharField(max_length=150)

    # Created and Updated Datetimes
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
