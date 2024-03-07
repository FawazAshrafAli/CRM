from django.urls import path
from .views  import CreateOrganizationView, ListOrganizationView, DetailOrganizationView, UpdateOrganizationView, DeleteOrganizationView

app_name = "organizations"

urlpatterns = [
    path('', ListOrganizationView.as_view(), name="list_organizations"),
    path('create_organization/', CreateOrganizationView.as_view(), name="create_organization"),
    path('detail_organization/<pk>', DetailOrganizationView.as_view(), name="detail_organization"),
    path('update_organization/<pk>', UpdateOrganizationView.as_view(), name="update_organization"),
    path('delete_organization/<pk>', DeleteOrganizationView.as_view(), name="delete_organization")
]
