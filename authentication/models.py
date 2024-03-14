from django.db import models
from django.contrib.auth.models import User

class CrmUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=16, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    address_city = models.CharField(max_length=150, null=True, blank=True)
    address_state = models.CharField(max_length=150, null=True, blank=True)
    address_postal_code = models.CharField(max_length=150, null=True, blank=True)
    address_country = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    reports_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports_to", blank=True, null=True)

    # Personal Information
    passport_number = models.CharField(max_length=25, null=True, blank=True)
    passport_expiry_date = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    maritial_status = models.CharField(max_length=75, null=True, blank=True)
    employment_of_spouse = models.CharField(max_length=150, null=True, blank=True)
    number_of_children = models.PositiveIntegerField(blank=True, null=True)

    # Emergency Contact
    primary_contact_name = models.CharField(max_length=100, null=True, blank=True)
    primary_contact_relationship = models.CharField(max_length=100, null=True, blank=True)
    priamry_contact_phone = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_name = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_relationship = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_phone = models.CharField(max_length=100, null=True, blank=True)

    # Bank information
    bank_name = models.CharField(max_length=150, null=True, blank=True)
    bank_account_number = models.CharField(max_length=25, null=True, blank=True)
    ifsc_code = models.CharField(max_length=25, null=True, blank=True)
    pan_number = models.CharField(max_length=25, null=True, blank=True)

    # Family Informations
    family_info = models.JSONField(blank=True, null=True)

    # Education Informations
    education_info = models.JSONField(blank=True, null=True)

    # Experience
    experience = models.JSONField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        self.user.username
