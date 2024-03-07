from django import forms
from .views import Lead

class LeadUpdationForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"