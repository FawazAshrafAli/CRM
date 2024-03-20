from django.shortcuts import render
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from  .models import Company
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from contacts.models import Contact
from projects.models import Project
from deals.models import Deal



class BaseOrganizationView(LoginRequiredMixin):
    model = Company
    login_url = 'authentication:login'


class CreateOrganizationView(BaseOrganizationView, CreateView):    
    template_name = 'organizations/companies.html'
    fields="__all__"
    success_url = reverse_lazy('organizations:list')
    raise_exception = True

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "New organization has been created!")
        return response
    
    def form_invalid(self, form):
        for field, errors in  form.errors.items():
            for error in errors:
                print(f"Error in {field} : {error}")
        messages.error(self.request, "Failed to create task.")
        return super().form_invalid(form)
    


class ListOrganizationView(BaseOrganizationView, ListView):    
    template_name = "organizations/companies.html"    
    context_object_name = "organizations"
    queryset = Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context.update({
            "contacts": Contact.objects.all(),
            "projects": Project.objects.all(),
            "deals": Deal.objects.all(),
            })
        return context
    


class DetailOrganizationView(BaseOrganizationView, DetailView):    
    template_name = "organizations/companies.html"
    query_pk_and_slug = 'pk'
    context_object_name = 'organization'

    def render_to_response(self, context, **response_kwargs):
        organization = context['object']

        serialized_data = {
            "id": organization.id,
            "name" : organization.name,
            "organization" : organization.organization,
            "title" : organization.title,
            "phone" : organization.phone,
            "fax" : organization.fax,
            "website" : organization.website,
            "linkedin" : organization.linkedin,
            "facebook" : organization.facebook,
            "twitter" : organization.twitter,
            "email_domains" : organization.email_domains,
            "billing_address" : f"{organization.billing_address}, {organization.billing_city}, {organization.billing_state}, {organization.billing_postal_code}, {organization.billing_country}.",                                
            "description" : organization.description,
            "tag_list" : organization.tag_list,
            "permission" : organization.permission,
            "created": organization.created.strftime("%d/%m/%Y"),
            "updated": organization.updated.strftime("%d/%m/%Y")
        }
        if organization.date_to_remember:
            date_to_remember = organization.date_to_remember.strftime("%d/%m/%Y")
            serialized_data["date_to_remember"] = date_to_remember

        if organization.shipping_address and organization.shipping_city and organization.shipping_state and organization.shipping_postal_code and organization.shipping_country :            
            shipping_address = f"{organization.shipping_address}, {organization.shipping_city}, {organization.shipping_state}, {organization.shipping_postal_code}, {organization.shipping_country}."
            serialized_data["shipping_address"] = shipping_address

        return JsonResponse(serialized_data)

class UpdateOrganizationView(BaseOrganizationView, UpdateView):    
    template_name = "organizations/companies.html"
    fields="__all__"
    pk_url_kwarg = 'pk'
    context_object_name = "organization"

    def form_valid(self, form):
        response = super().form_valid(form)
        # messages.success(self.request, "Company Updated.")
        return response

    def get_success_url(self):
        return reverse_lazy('organizations:detail', kwargs={'pk' : self.object.pk})    


class DeleteOrganizationView(BaseOrganizationView, DeleteView):    
    template_name = "organizations/confirm_deletion.html"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('organizations:list')
    context_object_name = 'organization'

