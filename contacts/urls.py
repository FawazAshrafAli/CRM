from django.urls import path
from .views import ListContactView, CreateContactView, UpdateContactView, DeleteContactView, DetailContactView

app_name = "contacts"

urlpatterns = [
    path('', ListContactView.as_view(),  name='list'),
    path('detail_contact/<pk>', DetailContactView.as_view(), name='detail_contact'),
    path('create_contact/', CreateContactView.as_view(), name='create_contact'),
    path('update_contact/<pk>', UpdateContactView.as_view(), name='update_contact'),
    path('delete_contact/<pk>', DeleteContactView.as_view(), name='delete_contact'),
]
