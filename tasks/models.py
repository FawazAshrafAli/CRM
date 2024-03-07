from django.db import models

class Task(models.Model):
    # task details
    name = models.CharField(max_length=200, blank=False, null=False)
    assigned_to = models.CharField(max_length=150, blank=True, null=True, default="Me")
    category = models.CharField(max_length=150, blank=True, null=True, default="Email")
    due_date = models.DateField()

    # additional information
    start_date = models.DateField()
    reminder_date = models.DateField()
    progress = models.CharField(max_length=150, blank=True, null=True)
    priority = models.CharField(max_length=150, blank=True, null=True, default="Low")
    status = models.CharField(max_length=150, default='Not Started')

    # related to
    related_to = models.CharField(max_length=150, blank=True, null=True)

    # description information
    description = models.TextField(blank=True, null=True)

    # Permissions
    permission = models.CharField(max_length=150, blank=False, null=False)

    percentage_completed = models.PositiveIntegerField(default = 0)    
    task_owner = models.CharField(max_length=150, blank=False, null=False)