from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http  import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils import timezone
from django.utils.timezone import timedelta
from django.contrib.auth.models import User

from authentication.models import CrmUser
from organizations.models import Company
from projects.models import Project
from deals.models import Deal
from leads.models import Lead
from .models import Contact


class BaseContactView(LoginRequiredMixin):
    login_url = 'authentication:login'
    model = Contact
    template_name = 'contacts/contacts.html'


class CreateContactView(BaseContactView, CreateView):    
    template_name = 'contacts/contacts.html'
    fields = "__all__"
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


class CloneContactView(BaseContactView, CreateView):
    fields = "__all__"
    success_url = reverse_lazy('contacts:list')

    def get_object(self):
        try:
            return get_object_or_404(Contact, pk=self.kwargs['pk'])
        except Http404:
            messages.error(self.request, "Invalid contact")
            return HttpResponseRedirect(reverse('contacts:list'))          

    def get(self, request, *args, **kwargs):        
        self.object = self.get_object()
        try:   
            Contact.objects.create(
                image = self.object.image,
                prefix = self.object.prefix,
                first_name = self.object.first_name,
                last_name = self.object.last_name,
                organization = self.object.organization,
                title = self.object.title,
                email = self.object.email,
                email_opted_out = self.object.email_opted_out,
                phone = self.object.phone,
                home_phone = self.object.home_phone,
                mobile_phone = self.object.mobile_phone,
                other_phone = self.object.other_phone,
                assistant_phone = self.object.assistant_phone,
                assistant_name = self.object.assistant_name,
                fax = self.object.fax,
                linkedin = self.object.linkedin,
                facebook = self.object.facebook,
                twitter = self.object.twitter,
                mailing_address = self.object.mailing_address,
                mailing_city = self.object.mailing_city,
                mailing_state = self.object.mailing_state,
                mailing_postal_code = self.object.mailing_postal_code,
                mailing_country = self.object.mailing_country,
                other_address = self.object.other_address,
                other_city = self.object.other_city,
                other_state = self.object.other_state,
                other_postal_code = self.object.other_postal_code,
                other_country = self.object.other_country,
                due_date = self.object.due_date,
                date_of_birth = self.object.date_of_birth,
                description = self.object.description,
                permission = self.object.permission,
                tag_list = self.object.tag_list,
                permissions = self.object.permissions,
            )
            messages.success(self.request, "Contact Cloned Successfully.")
            return redirect(self.get_success_url())        
        except Exception as e:
            messages.error(self.request, f"Failed to clone contact: {e}")
            return redirect('contacts:list')
        
        
class ListContactView(BaseContactView, ListView):
    template_name = 'contacts/contacts.html'    
    context_object_name = "contacts"
    queryset = Contact.objects.filter(archived = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'organizations' : Company.objects.all(),
            'related_contacts': Contact.objects.all(),
            'deals': Deal.objects.all(),
            'projects': Project.objects.all(),
            'users': CrmUser.objects.all()
        })
        return context
    

class ListCreatedLastDayContactView(ListContactView):    
    queryset = Contact.objects.filter(archived = False, created__gt = timezone.now() - timedelta(days=1))


class ListLastWeekContactView(ListContactView):    
    queryset = Contact.objects.filter(archived = False, created__gt = timezone.now() - timedelta(days=7))
    

class DetailContactView(BaseContactView, DetailView):
    template_name = 'contacts/contacts.html'
    query_pk_and_slug = 'pk'

    def render_to_response(self, context, **response_kwargs):
        contact = context['object']

        serialized_data = {}

        # Auto dictionary creation using field name in a model and their respective value
        for field in contact._meta.fields:
            field_name = field.name
            if field_name not in ("organization", "created", "updated", "image", "record_owner"):
                field_value = getattr(contact, field_name)
                serialized_data[field_name] = field_value        

        if contact.image:
            serialized_data['image'] = contact.image.url

        # Compining names together to form full name
        if contact.first_name and contact.last_name:
            serialized_data["full_name"] = f"{contact.first_name} {contact.last_name}"
        elif contact.first_name:
            serialized_data["full_name"] = contact.first_name

        if contact.organization:
            serialized_data.update({
                "organization_id" : contact.organization.id,
                "organization" : contact.organization.name
                })            

        # Combining all fields of mailing addres to form full mailing address
        if contact.mailing_address and contact.mailing_city and contact.mailing_state and contact.mailing_postal_code and contact.mailing_country:
            mailing_address = f"{contact.mailing_address}, {contact.mailing_city}, {contact.mailing_state}, {contact.mailing_postal_code}, {contact.mailing_country}."
            serialized_data['mailing_address'] = mailing_address

        # Combining all fields of other addres to form full mailing address
        if contact.other_address and contact.other_city and contact.other_state and contact.other_postal_code and contact.other_country:
            other_address = f"{contact.other_address}, {contact.other_city}, {contact.other_state}, {contact.other_postal_code}, {contact.other_country}."
            serialized_data['other_address'] = other_address

        if contact.record_owner:
            serialized_data.update({
                'record_owner': contact.record_owner.id,
                'record_owner_name': contact.record_owner.name
                })

        serialized_data.update({
            'created' : contact.created.strftime("%b %d, %Y"),
            'updated' : contact.updated.strftime("%d/%m/%Y")
            })

        return JsonResponse(serialized_data)


class UpdateContactView(BaseContactView, UpdateView):
    model = Contact
    fields = "__all__"
    pk_url_kwarg = 'pk'
    context_object_name = "contact"
    success_url = reverse_lazy('contacts:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Contact Updated.")
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():            
            for error in errors:
                print(f"Error in field {field}: {error}")
        return redirect(reverse_lazy('authentication:error500'))
    

class UpdateContactImageView(BaseContactView, UpdateView):
    fields = ["image"]
    success_url = reverse_lazy('contacts:list')

    def form_valid(self, form):
        messages.success(self.request, "Contact image updated successfully")
        return super().form_valid(form)


class UpdateContactOwner(BaseContactView, UpdateView):
    modal = Contact
    fields = ["record_owner"]
    success_url = reverse_lazy('contacts:list')

    def form_valid(self, form):
        messages.success(self.request, "Record owner updated successfully.")
        return super().form_valid(form)


class DeleteContactView(BaseContactView, DeleteView):
    model = Contact
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('contacts:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()            
            return redirect(self.get_success_url())
        except Exception as e:
            messages.error(self.request, f"Failed to delete contact due to {e}")
            return HttpResponseRedirect(reverse('contact:list'))
        

    def form_valid(self, form):
        messages.success(self.request, "Contact Deleted Successfully.")
        return super().form_valid(form)
    

class LeadConvertionView(BaseContactView, CreateView):
    modal = Lead
    fields = "__all__"
    success_url = reverse_lazy('contacts:list')

    def get_object(self, **kwargs):
        try:
            return get_object_or_404(Contact, pk = self.kwargs['pk'])            
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))
        
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        try:
            get_object_or_404(Lead, organization = self.object.organization, email = self.object.email, phone = self.object.phone)
            messages.warning(self.request, "Lead already exists.")
            return redirect(reverse_lazy('contacts:list'))
        except Http404:
            pass

        try:
            Lead.objects.create(
                image = self.object.image,
                prefix = self.object.prefix,
                first_name = self.object.first_name,
                last_name = self.object.last_name,
                organization = self.object.organization,
                title = self.object.title,                
                lead_owner = self.object.record_owner,
                email = self.object.email,
                email_opted_out = self.object.email_opted_out,
                phone = self.object.phone,
                mobile_phone = self.object.mobile_phone,
                fax = self.object.fax,                
                mailing_address = self.object.mobile_phone,
                mailing_city = self.object.mobile_phone,
                mailing_state = self.object.mobile_phone,
                mailing_postal_code = self.object.mobile_phone,
                mailing_country = self.object.mobile_phone,
                description = self.object.description,
                tag_list =  self.object.tag_list
            )
            self.object.archived = True
            self.object.save()
            messages.success(self.request, "Contact has been changed to deal.")
            return redirect(self.get_success_url())
        except Exception as e:
            print(e)
            return redirect(reverse_lazy('authentication:error500'))
        
    def form_valid(self, form):
        messages.success(self.request, "Contact successfully converted to lead.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error on {field}: {error}")
        return redirect(reverse_lazy('authentication:error500'))