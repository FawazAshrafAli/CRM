from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

from authentication.models import CrmUser

class BaseDashboardView(LoginRequiredMixin):
    login_url='authentication:login'

    def get_context_data(self):
        context = {}
        try:
            context['user'] = get_object_or_404(CrmUser, user = self.request.user)
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))
        return context


class DealsDashboardView(BaseDashboardView, TemplateView):
    template_name = 'dashboard/deals-dashboard.html'


class LeadsDashboardView(BaseDashboardView, TemplateView):    
    template_name = 'dashboard/leads-dashboard.html'


class ProjectsDashboardView(BaseDashboardView, TemplateView):    
    template_name = 'dashboard/projects-dashboard.html'

