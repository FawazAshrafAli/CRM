from django.urls import path
from .views  import (CreateOrganizationView, ListOrganizationView, 
                     DetailOrganizationView, UpdateOrganizationView, 
                     DeleteOrganizationView, ChangeOrganizationImageView, 
                     ChangeOrganizationRecordOwnerView, ListOrganizationCreatedLastDayView, 
                     ListOrganizationCreatedLastWeekView, CreateRecentlyViewedOrganizationView,
                     ListRecentlyViewedOrganizationView)

app_name = "organizations"

urlpatterns = [
    path('', ListOrganizationView.as_view(), name="list"),
    path('list/last_24_hours/', ListOrganizationCreatedLastDayView.as_view(), name="last_24_hours"),
    path('list/last_7_days/', ListOrganizationCreatedLastWeekView.as_view(), name="last_7_days"),
    path('list/recently_viewed/', ListRecentlyViewedOrganizationView.as_view(), name="recently_viewed"),
    path('create/', CreateOrganizationView.as_view(), name="create"),
    path('update_recently_viewed/<pk>', CreateRecentlyViewedOrganizationView.as_view(), name="update_recently_viewed"),
    path('detail/<pk>', DetailOrganizationView.as_view(), name="detail"),
    path('update/<pk>', UpdateOrganizationView.as_view(), name="update"),    
    path('change_image/<pk>', ChangeOrganizationImageView.as_view(), name="change_image"),
    path('change_owner/<pk>', ChangeOrganizationRecordOwnerView.as_view(), name="change_owner"),
    path('delete/<pk>', DeleteOrganizationView.as_view(), name="delete")
]
