from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Report

class BaseReportView(LoginRequiredMixin):
    login_url = 'login'
    model = Report


class ReportListView(BaseReportView, ListView):
    template_name = "reports/reports.html"
    queryset = Report.objects.all()