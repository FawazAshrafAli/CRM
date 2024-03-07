from django.test import TestCase
from . import forms

class LeadUpdationFormTestCase(TestCase):
    def test_form_validation(self):
        # Provide valid or invalid form data as a dictionary
        form_data = {
            'prefix': 'Mr',  # Replace 'field1' with an actual field name from your form
            'first_name': 'David',  # Replace 'field2' with another field name
            # Add more fields and values as needed
        }

        form = forms.LeadUpdationForm(data=form_data)
        self.assertTrue(form.is_valid())
        # Add more assertions based on your form's behavior
