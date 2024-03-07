from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseDashboardView(LoginRequiredMixin):
    login_url='authentication:login'


class DealsDashboardView(BaseDashboardView, TemplateView):
    template_name = 'dashboard/deals-dashboard.html'


class LeadsDashboardView(BaseDashboardView, TemplateView):    
    template_name = 'dashboard/leads-dashboard.html'


class ProjectsDashboardView(BaseDashboardView, TemplateView):    
    template_name = 'dashboard/projects-dashboard.html'

