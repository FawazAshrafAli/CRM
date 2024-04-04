from django.urls import path
from .views  import (CreateDealView, UpdateDealView, ListDealView, 
                     DetailDealView, DeleteDealView, UpdateDealImageView, 
                     CloneDealView, UpdateDealOwnerView, DealToLeadView)

app_name = "deals"

urlpatterns = [
    path('', ListDealView.as_view(), name='list'),
    path('create/', CreateDealView.as_view(), name='create'),
    path('clone_deal/<pk>', CloneDealView.as_view(), name='clone_deal'),
    path('detail/<pk>', DetailDealView.as_view(), name="detail"),
    path('update/<pk>', UpdateDealView.as_view(), name= 'update'),
    path('update_image/<pk>', UpdateDealImageView.as_view(), name= 'update_image'),
    path('update_owner/<pk>', UpdateDealOwnerView.as_view(), name= 'update_owner'),
    path('delete/<pk>', DeleteDealView.as_view(), name='delete'),
    path('convert_to_lead/<pk>', DealToLeadView.as_view(), name='convert_to_lead'),
]
