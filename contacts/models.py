from django.db import models

class Contact(models.Model):
    # name and occupation
    prefix = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    organization = models.CharField(max_length=150, blank=False, null=False)
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
    mailing_address = models.TextField()
    mailing_city = models.CharField(max_length=50, blank=True, null=True)
    mailing_state = models.CharField(max_length=50, blank=True, null=True)
    mailing_postal_code = models.CharField(max_length=15, blank=True, null=True)
    mailing_country = models.CharField(max_length=100, blank=True, null=True, default="India")
    other_address = models.TextField()
    other_city = models.CharField(max_length=50, blank=True, null=True)
    other_state = models.CharField(max_length=50, blank=True, null=True)
    other_postal_code = models.CharField(max_length=15, blank=True, null=True)
    other_country = models.CharField(max_length=100, blank=True, null=True, default="India")

    # dates to remember
    due_date = models.DateField()
    date_of_birth = models.DateField()

    # description information
    description = models.TextField()

    # permission
    permission = models.CharField(max_length=100, blank=True, null=True)

    # tag information
    tag_list = models.CharField(max_length=150)

    # permissions
    permissions = models.CharField(max_length=150)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)