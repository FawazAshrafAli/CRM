from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
from django.http  import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from organizations.models import Company
from django.http import JsonResponse
from organizations.models import Company
from deals.models import Deal
from projects.models import Project

class BaseContactView(LoginRequiredMixin):
    login_url = 'authentication:login'
    model = Contact


class CreateContactView(BaseContactView, CreateView):    
    template_name = 'contacts/contacts.html'
    fields = [
        "prefix", "first_name", "last_name", "organization", "title", "email", "email_opted_out",
        "phone", "home_phone", "mobile_phone", "other_phone", "assistant_phone", "assistant_name",
        "fax", "linkedin", "facebook", "twitter", "mailing_address", "mailing_city", "mailing_state",
        "mailing_postal_code", "mailing_country", "other_address", "other_city", "other_state",
        "other_postal_code", "other_country", "due_date", "date_of_birth", "description", "permission",
        "tag_list"
    ]
    success_url = reverse_lazy('contacts:list')    

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "New contact has been created!")
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        for field, errors  in form.errors.items():
            for error in errors:
                print(f"Error on {field}: {error}")
        return response



class ListContactView(BaseContactView, ListView):
    template_name = 'contacts/contacts.html'
    queryset = Contact.objects.all()
    context_object_name = "contacts"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'organizations' : Company.objects.all(),
            'contacts': Contact.objects.all(),
            'deals': Deal.objects.all(),
            'projects': Project.objects.all(),
        })
        return context


class DetailContactView(BaseContactView, DetailView):
    template_name = 'contacts/contacts.html'
    query_pk_and_slug = 'pk'

    def render_to_response(self, context, **response_kwargs):
        contact = context['object']

        serialized_data = {}

        # Auto dictionary creation using field name in a model and their respective value
        for field in contact._meta.fields:
            field_name = field.name
            if field_name not in ("organization", "created", "updated"):
                field_value = getattr(contact, field_name)
                serialized_data[field_name] = field_value        

        # Compining names together to form full name
        if contact.first_name and contact.last_name:
            serialized_data["full_name"] = f"{contact.first_name} {contact.last_name}"
        elif contact.first_name:
            serialized_data["full_name"] = contact.first_name

        if contact.organization:
            serialized_data["organization"] = contact.organization.name            

        # Combining all fields of mailing addres to form full mailing address
        if contact.mailing_address and contact.mailing_city and contact.mailing_state and contact.mailing_postal_code and contact.mailing_country:
            mailing_address = f"{contact.mailing_address}, {contact.mailing_city}, {contact.mailing_state}, {contact.mailing_postal_code}, {contact.mailing_country}."
            serialized_data['mailing_address'] = mailing_address

        # Combining all fields of other addres to form full mailing address
        if contact.other_address and contact.other_city and contact.other_state and contact.other_postal_code and contact.other_country:
            other_address = f"{contact.other_address}, {contact.other_city}, {contact.other_state}, {contact.other_postal_code}, {contact.other_country}."
            serialized_data['other_address'] = other_address

        if contact.due_date:
            due_date = contact.due_date.strftime("%d/%m/%Y")
            serialized_data['due_date'] = due_date

        if contact.date_of_birth:
            date_of_birth = contact.date_of_birth.strftime("%d/%m/%Y")
            serialized_data['date_of_birth'] = date_of_birth

        serialized_data.update({
            'created' : contact.created.strftime("%b %d, %Y"),
            'updated' : contact.updated.strftime("%d/%m/%Y")
            })

        return JsonResponse(serialized_data)


class UpdateContactView(BaseContactView, UpdateView):
    template_name = 'contacts/update_contact.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'
    context_object_name = "contact"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Contact Updated.")
        return response

    def get_success_url(self):
        return reverse_lazy('detail_contact', kwargs={'pk' : self.object.pk})    


class DeleteContactView(LoginRequiredMixin, DeleteView):
    template_name = 'contacts/confirm_deletion.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('list_contacts')
    context_object_name = 'contact'