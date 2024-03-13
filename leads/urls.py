from django.urls import path
from .views import ListLeadView,  CreateLeadView, UpdateLeadView, DeleteLeadView, DetailLeadView

app_name= 'leads'

urlpatterns = [
    path('', ListLeadView.as_view(), name='list'),
    path('create/', CreateLeadView.as_view(), name='create'),
    path('detail/<pk>', DetailLeadView.as_view(), name="detail"),
    path('update/<pk>', UpdateLeadView.as_view(), name= 'update'),
    path('delete/<pk>', DeleteLeadView.as_view(), name='delete'),
]
