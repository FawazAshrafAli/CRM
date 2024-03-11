from django.shortcuts import render
from django.views.generic import ListView
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseActivityView(LoginRequiredMixin):
    login_url = 'authentication:login'
    model = Activity

class ActivityListView(BaseActivityView, ListView):
    template_name = "activities/activities.html"
    queryset = Activity.objects.all()