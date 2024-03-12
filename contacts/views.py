from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
from django.http  import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseContactView(LoginRequiredMixin):
    login_url = 'authentication:login'
    model = Contact


class CreateContactView(BaseContactView, CreateView):    
    template_name = 'contacts/create_contact.html'
    fields = [
        "prefix", "first_name", "last_name", "organization", "title", "email", "email_opted_out",
        "phone", "home_phone", "mobile_phone", "other_phone", "assistant_phone", "assistant_name",
        "fax", "linkedin", "facebook", "twitter", "mailing_address", "mailing_city", "mailing_state",
        "mailing_postal_code", "mailing_country", "other_address", "other_city", "other_state",
        "other_postal_code", "other_country", "due_date", "date_of_birth", "description", "permission",
        "tag_list", "task_visibility"
    ]
    success_url = reverse_lazy('create_contact')    

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "New contact has been created!")
        return response


class ListContactView(BaseContactView, ListView):
    template_name = 'contacts/contacts.html'
    queryset = Contact.objects.all()
    context_object_name = "contacts"


class DetailContactView(BaseContactView, DetailView):
    template_name = 'contacts/detail_contact.html'
    query_pk_and_slug = 'pk'
    context_object_name = 'contact'


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