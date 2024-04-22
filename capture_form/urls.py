from django.urls import path
from .views import FormView, CreateLeadView

app_name = 'capture_form'

urlpatterns = [
    path('form/', FormView.as_view(), name="form"),
    path('create_lead/', CreateLeadView.as_view(), name="create_lead"),
]
