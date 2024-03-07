from django import forms
from .models import Task

class  ContactCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class  ContactUpdationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"