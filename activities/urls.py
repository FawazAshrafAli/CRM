from django.urls import path
from .views import ActivityListView

app_name = "activities"

urlpatterns = [
    path('', ActivityListView.as_view(), name="list"),
]
