from django.db import models
from authentication.models import CrmUser
from django.utils import timezone

class PipelineStage(models.Model):
    stage = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.stage
    

class Project(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    status = models.CharField(max_length=150, blank=False, null=False, default="In Progress")
    category = models.CharField(max_length=150, blank=False, null=False, default="Email")
    user_responsible = models.ForeignKey(CrmUser, on_delete=models.PROTECT, blank=False, null=False)

    # Pipeline and Stage
    pipeline = models.CharField(max_length=150, blank=False, null=False)
    stage = models.ManyToManyField(PipelineStage)

    # Description Information
    description = models.TextField(blank=True, null=True)

    # Tag Information
    tag_list = models.CharField(max_length=250)

    # Permissions
    visibility = models.CharField(max_length=150, blank=False, null=False)
    
    # Created and Updated Datetime
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
