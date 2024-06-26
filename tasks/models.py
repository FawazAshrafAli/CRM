from django.db import models
from authentication.models import CrmUser
class Task(models.Model):
    # task details
    name = models.CharField(max_length=200, blank=False, null=False)
    assigned_to = models.ForeignKey(CrmUser, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True, default="Email")
    due_date = models.CharField(max_length=50, blank=True, null=True)

    # additional information
    start_date = models.CharField(max_length=50, blank=True, null=True)
    reminder_date = models.CharField(max_length=50, blank=True, null=True)
    progress = models.PositiveIntegerField(default=0)
    priority = models.CharField(max_length=150, blank=True, null=True, default="Low")
    status = models.CharField(max_length=150, default='Not Started')
        
    # related to
    related_to = models.CharField(max_length=150, blank=True, null=True)

    # description information
    description = models.TextField(blank=True, null=True)
    
    # Task Owner
    record_owner = models.ForeignKey(CrmUser, on_delete=models.CASCADE, blank=True, null=True, related_name="task_owner")

    # Persmission
    task_visibility = models.CharField(max_length=150, blank=True, null=True)

    created_by = models.ForeignKey(CrmUser, on_delete=models.CASCADE, blank=True, null=True, related_name="task_created_by")

    #  Creation and Updation Details
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)