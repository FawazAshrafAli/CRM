from django.db import models
from django.contrib.auth.models import User

class CrmUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=16, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        self.user.username
