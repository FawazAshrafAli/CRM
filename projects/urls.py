from django.urls import path
from .views import (ProjectListView, ProjectCreateView, 
                    ProjectDetailView, ProjectStageUpdateView, 
                    ProjectUpdateView, ProjectImageUpdateView, 
                    ProjectCloneView, ProjectDeleteView, 
                    ProjectOwnerUpdateView)

app_name = "projects"

urlpatterns = [
    path('', ProjectListView.as_view(), name="list"),
    path('create/', ProjectCreateView.as_view(), name="create"),
    path('clone/<pk>', ProjectCloneView.as_view(), name="clone"),
    path('update/<pk>', ProjectUpdateView.as_view(), name="update"),
    path('update_image/<pk>', ProjectImageUpdateView.as_view(), name="update_image"),
    path('update_owner/<pk>', ProjectOwnerUpdateView.as_view(), name="update_owner"),
    path('detail/<pk>', ProjectDetailView.as_view(), name="detail"),    
    path('update_stage/<pk>', ProjectStageUpdateView.as_view(), name="update_stage"),
    path('delete/<pk>', ProjectDeleteView.as_view(), name="delete"),
]
