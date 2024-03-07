from django.urls import path
from .views import DealsDashboardView, LeadsDashboardView, ProjectsDashboardView

app_name = "dashboard"

urlpatterns = [
    path('', DealsDashboardView.as_view(), name="deals_dashboard"),
    path('leads_dashboard/', LeadsDashboardView.as_view(), name="leads_dashboard"),
    path('projects_dashboard/', ProjectsDashboardView.as_view(), name="projects_dashboard"),
]
