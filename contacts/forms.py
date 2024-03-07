from django import forms
from .models import Contact

class ContactCreationForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactUpdationForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"