from django.db import models
from django.contrib.auth.models import User

class CrmUserFamilyInformation(models.Model):
    crm_user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    relationship = models.CharField(max_length=150)
    date_of_birth = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class CrmUserEducation(models.Model):
    crm_user_id = models.CharField(max_length=50)
    institution = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    started_year = models.CharField(max_length=50)
    completed_year = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['started_year']

class CrmUserExperience(models.Model):
    crm_user_id = models.CharField(max_length=50)
    designation = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    started_month_and_year = models.CharField(max_length=50)
    completed_month_and_year = models.CharField(max_length=50, blank=True, null=True)

class CrmUser(models.Model):
    image = models.ImageField(upload_to="crm_user_images/", blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    birthday = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    address_city = models.CharField(max_length=150, null=True, blank=True)
    address_state = models.CharField(max_length=150, null=True, blank=True)
    address_postal_code = models.CharField(max_length=150, null=True, blank=True)
    address_country = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    team = models.CharField(max_length=150, null=True, blank=True)
    reports_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    # Personal Information
    passport_number = models.CharField(max_length=25, null=True, blank=True, unique=True)
    passport_expiry_date = models.CharField(max_length=50, null=True, blank=True)
    tel = models.CharField(max_length=16, null=True, blank=True, unique=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=75, null=True, blank=True)
    employment_of_spouse = models.CharField(max_length=150, null=True, blank=True)
    number_of_children = models.PositiveIntegerField(blank=True, null=True)

    # Emergency Contact
    primary_contact_name = models.CharField(max_length=100, null=True, blank=True)
    primary_contact_relationship = models.CharField(max_length=100, null=True, blank=True)
    primary_contact_phone1 = models.CharField(max_length=100, null=True, blank=True)
    primary_contact_phone2 = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_name = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_relationship = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_phone1 = models.CharField(max_length=100, null=True, blank=True)
    secondary_contact_phone2 = models.CharField(max_length=100, null=True, blank=True)

    # Bank information
    bank_name = models.CharField(max_length=150, null=True, blank=True)
    bank_account_number = models.CharField(max_length=25, null=True, blank=True)
    ifsc_code = models.CharField(max_length=25, null=True, blank=True)
    pan_number = models.CharField(max_length=25, null=True, blank=True)

    # Family Informations
    family_info = models.ManyToManyField(CrmUserFamilyInformation)

    # Education Informations
    education_info = models.ManyToManyField(CrmUserEducation)

    # Experience
    experience = models.ManyToManyField(CrmUserExperience)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return self.user.first_name
 