from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    status = models.CharField(max_length=150, blank=False, null=False, default="In Progress")
    category = models.CharField(max_length=150, blank=False, null=False, default="Email")
    user_responsible = models.CharField(max_length=150, blank=False, null=False)

    # Pipeline and Stage
    pipeline = models.CharField(max_length=150, blank=False, null=False)
    stage = models.CharField(max_length=150, blank=False, null=False)

    # Description Information
    description = models.TextField()

    # Tag Information
    tag_list = models.CharField(max_length=250)

    # Permissions
    visibility = models.CharField(max_length=150, blank=False, null=False)
    
    # Created and Updated Datetime
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
