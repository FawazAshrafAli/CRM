from django.urls import path
from .views  import CreateDealView, UpdateDealView, ListDealView, DetailDealView, DeleteDealView

app_name = "deals"

urlpatterns = [
    path('', ListDealView.as_view(), name='list'),
    path('create/', CreateDealView.as_view(), name='create'),
    path('detail/<pk>', DetailDealView.as_view(), name="detail"),
    path('update/<pk>', UpdateDealView.as_view(), name= 'update'),
    path('delete/<pk>', DeleteDealView.as_view(), name='delete'),
]
