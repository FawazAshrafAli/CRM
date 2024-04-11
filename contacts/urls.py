from django.urls import path
from .views import (ListContactView, CreateContactView, 
                    UpdateContactView, DeleteContactView, 
                    DetailContactView, UpdateContactImageView,
                    CloneContactView, UpdateContactOwner, 
                    LeadConvertionView, ListLastWeekContactView, 
                    ListCreatedLastDayContactView)

app_name = "contacts"

urlpatterns = [
    path('', ListContactView.as_view(),  name='list'),
    path('list/last_24_hours/', ListCreatedLastDayContactView.as_view(),  name='list_24_hours'),
    path('list/last_7_days/', ListLastWeekContactView.as_view(),  name='list_7_days'),
    path('detail/<pk>', DetailContactView.as_view(), name='detail'),
    path('create/', CreateContactView.as_view(), name='create'),
    path('clone/<pk>', CloneContactView.as_view(), name='clone'),
    path('update/<pk>', UpdateContactView.as_view(), name='update'),
    path('update_image/<pk>', UpdateContactImageView.as_view(), name='update_image'),
    path('update_contact_owner/<pk>', UpdateContactOwner.as_view(), name='update_contact_owner'),
    path('lead_convertion/<pk>', LeadConvertionView.as_view(), name='lead_convertion'),
    path('delete/<pk>', DeleteContactView.as_view(), name='delete'),
]
