from django.db import models
from organizations.models import Company
from authentication.models import CrmUser

class Contact(models.Model):
    # name and occupation
    image = models.ImageField(upload_to='contact_photos/', null=True, blank=True)
    prefix = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=True, null=True)    
    organization = models.ForeignKey(Company, on_delete=models.PROTECT)
    title = models.CharField(max_length=150, blank=False, null=False)

    # contact details
    email = models.EmailField(max_length=254, blank=False, null=False)
    email_opted_out = models.BooleanField(default=False)
    phone = models.CharField(max_length=16, blank=False, null=False)
    home_phone = models.CharField(max_length=16, blank=True, null=True)
    mobile_phone = models.CharField(max_length=16, blank=False, null=False)
    other_phone = models.CharField(max_length=16, blank=True, null=True)
    assistant_phone = models.CharField(max_length=16, blank=True, null=True)
    assistant_name = models.CharField(max_length=150, blank=True, null=True)
    fax = models.CharField(max_length=25, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)

    # address information
    mailing_address = models.TextField(blank=False, null=False)
    mailing_city = models.CharField(max_length=50, blank=False, null=False)
    mailing_state = models.CharField(max_length=50, blank=False, null=False)
    mailing_postal_code = models.CharField(max_length=15, blank=False, null=False)
    mailing_country = models.CharField(max_length=100, blank=False, null=False)
    other_address = models.TextField(blank=True, null=True)
    other_city = models.CharField(max_length=50, blank=True, null=True)
    other_state = models.CharField(max_length=50, blank=True, null=True)
    other_postal_code = models.CharField(max_length=15, blank=True, null=True)
    other_country = models.CharField(max_length=100, blank=True, null=True)

    # dates to remember
    due_date = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, blank=True, null=True)

    # description information
    description = models.TextField(blank=True, null=True)

    # permission
    permission = models.CharField(max_length=100, blank=True, null=True)

    # tag information
    tag_list = models.CharField(max_length=150, blank=True, null=True)

    # permissions
    permissions = models.CharField(max_length=150, blank=True, null=True)

    record_owner = models.ForeignKey(CrmUser, on_delete=models.CASCADE, blank=True, null=True)

    archived = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)