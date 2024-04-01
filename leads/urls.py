from django.urls import path
from .views import (ListLeadView,  CreateLeadView, 
                    UpdateLeadView, UpdateLeadStatusView, 
                    DeleteLeadView, DetailLeadView, 
                    UpdateLeadImageView, CloneLeadView, 
                    ChangeLeadOwnerView, ChangeLeadToContact, 
                    ChangeLeadToDeal)

app_name= 'leads'

urlpatterns = [
    path('', ListLeadView.as_view(), name='list'),
    path('create/', CreateLeadView.as_view(), name='create'),
    path('clone_lead/<pk>', CloneLeadView.as_view(), name='clone_lead'),
    path('detail/<pk>', DetailLeadView.as_view(), name="detail"),
    path('update/<pk>', UpdateLeadView.as_view(), name= 'update'),
    path('update_image/<pk>', UpdateLeadImageView.as_view(), name= 'update_image'),
    path('update_owner/<pk>', ChangeLeadOwnerView.as_view(), name= 'update_owner'),
    path('update_lead_status/<pk>', UpdateLeadStatusView.as_view(), name= 'update_lead_status'),
    path('covert_to_contact/<pk>', ChangeLeadToContact.as_view(), name= 'covert_to_contact'),
    path('covert_to_deal/<pk>', ChangeLeadToDeal.as_view(), name= 'covert_to_deal'),
    path('delete/<pk>', DeleteLeadView.as_view(), name='delete'),
]
