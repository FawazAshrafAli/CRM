from django.urls import path
from .views import ListContactView, CreateContactView, UpdateContactView, DeleteContactView, DetailContactView

app_name = "contacts"

urlpatterns = [
    path('', ListContactView.as_view(),  name='list'),
    path('detail/<pk>', DetailContactView.as_view(), name='detail'),
    path('create/', CreateContactView.as_view(), name='create'),
    path('update/<pk>', UpdateContactView.as_view(), name='update'),
    path('delete/<pk>', DeleteContactView.as_view(), name='delete'),
]
