from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectDetailView

app_name = "projects"

urlpatterns = [
    path('', ProjectListView.as_view(), name="list"),
    path('create/', ProjectCreateView.as_view(), name="create"),
    path('detail/<pk>', ProjectDetailView.as_view(), name="detail"),
]
