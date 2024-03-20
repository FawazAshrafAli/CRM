from django.db import models

class Activity(models.Model):
    activity = models.CharField(max_length=150, blank=False, null=False)
    starting_date = models.DateField()
    starting_time = models.TimeField()
    ending_date = models.DateField()
    ending_time = models.TimeField()

    availability = models.CharField(max_length=150, blank=True, null=True, default="Busy")
    notes = models.TextField()

    user_responsible = models.CharField(max_length=150, blank=False, null=False)
    deal_or_lead = models.CharField(max_length=150, blank=False, null=False)
    people = models.CharField(max_length=250, blank=False, null=False)
    organization = models.CharField(max_length=150, blank=False, null=False)

    # meeting_follow_up_action = models.CharField(max_length=150, blank=True, null=True)

    # # Meeting
    # meeting_organizer = models.CharField(max_length=150, blank=True, null=True)
    # meeting_title = models.CharField(max_length=150, blank=True, null=True)
    # meeting_location = models.CharField(max_length=150, blank=True, null=True)
    # meeting_participants = models.JSONField(blank=True, null=True, default=list)
    # meeting_purpose = models.CharField(max_length=150, blank=True, null=True)
    # meeting_notes = models.TextField(blank=True, null=True)    

    # # Lunch/Meal
    # meal_organizer = models.CharField(max_length=150, blank=True, null=True)
    # mead_title = models.CharField(max_length=150, blank=True, null=True)    
    # meal_location = models.CharField(max_length=150, blank=True, null=True)    
    # meal_attendees = models.JSONField(blank=True, null=True, default=list)
    # meal_menu = models.JSONField(blank=True, null=True, default=list)
    # meal_purpose = models.CharField(max_length=150, blank=True, null=True)    
    # meal_special_requirements = models.TextField(blank=True, null=True)

    # # Flagged
    # Title = models.CharField(max_length=150, blank=True, null=True)    
    # flagged_datetime = models.DateTimeField(null=True, blank=True)
    # reason_for_flagging = models.TextField(blank=True, null=True)
    # flag_type = models.CharField(max_length=150, blank=True, null=True)    #e.g., priority level, status    
    # flagged_user = models.CharField(max_length=150, blank=True, null=True)    
    # due_date = models.DateField(null=True, blank=True)
    # Status = models.CharField(max_length=150, blank=True, null=True)     # open/completed/dismissed

