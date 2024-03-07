from django.urls import path
from .views  import CreateDealView, UpdateDealView, ListDealView, DetailDealView, DeleteDealView

urlpatterns = [
    path('', ListDealView.as_view(), name='list_deals'),
    path('create_deal/', CreateDealView.as_view(), name='create_deal'),
    path('detail_deal/<pk>', DetailDealView.as_view(), name="detail_deal"),
    path('update_deal/<pk>', UpdateDealView.as_view(), name= 'update_deal'),
    path('delete_deal/<pk>', DeleteDealView.as_view(), name='delete_deal'),
]
