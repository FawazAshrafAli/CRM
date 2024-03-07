from django.urls import path
from .views import ListLeadView,  CreateLeadView, UpdateLeadView, DeleteLeadView, DetailLeadView

urlpatterns = [
    path('', ListLeadView.as_view(), name='list_leads'),
    path('create_lead/', CreateLeadView.as_view(), name='create_lead'),
    path('detail_lead/<pk>', DetailLeadView.as_view(), name="detail_lead"),
    path('update_lead/<pk>', UpdateLeadView.as_view(), name= 'update_lead'),
    path('delete_lead/<pk>', DeleteLeadView.as_view(), name='delete_lead'),
]
