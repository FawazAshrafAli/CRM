from django.urls import path
from .views  import CreateOrganizationView, ListOrganizationView, DetailOrganizationView, UpdateOrganizationView, DeleteOrganizationView

app_name = "organizations"

urlpatterns = [
    path('', ListOrganizationView.as_view(), name="list"),
    path('create/', CreateOrganizationView.as_view(), name="create"),
    path('detail/<pk>', DetailOrganizationView.as_view(), name="detail"),
    path('update/<pk>', UpdateOrganizationView.as_view(), name="update"),
    path('delete/<pk>', DeleteOrganizationView.as_view(), name="delete")
]
