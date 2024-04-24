from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import ProtectedError
from django.utils import timezone
from django.utils.timezone import timedelta
from django.http import Http404
from pycountry import countries

from .models import Company, CompanyRecentlyViewed
from contacts.models import Contact
from projects.models import Project
from deals.models import Deal
from authentication.models import CrmUser


class BaseOrganizationView(LoginRequiredMixin):
    model = Company
    template_name = "organizations/companies.html"
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
    

class CreateRecentlyViewedOrganizationView(BaseOrganizationView, CreateView):
    model = CompanyRecentlyViewed
    fields = "__all__"

    def get_object(self, **kwargs):
        try:
            return get_object_or_404(Company, pk = self.kwargs['pk'])
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.user = request.user
        try:
            lookup_kwargs = {
                'company_object' : self.object,
                'user_object' : self.user
            }
            defaults = {
                'company_object' : self.object,
                'user_object' : self.user
            }
            CompanyRecentlyViewed.objects.update_or_create(
                defaults= defaults,
                **lookup_kwargs
            )
            return JsonResponse({'message' : 'success'})
        except Exception as e:
            print(e)
            return redirect(reverse_lazy('authentication:error500'))
    
        
            

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
            "users": CrmUser.objects.all(),
            "countries": [country.name for country in countries],
            })
        return context
    

class ListOrganizationCreatedLastDayView(ListOrganizationView):
    queryset = Company.objects.filter(created__gt = timezone.now() - timedelta(days=1))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_24_hours'] = True
        return context
    

class ListOrganizationCreatedLastWeekView(ListOrganizationView):
    queryset = Company.objects.filter(created__gt = timezone.now() - timedelta(days=7))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_7_days'] = True
        return context
    

class ListRecentlyViewedOrganizationView(ListOrganizationView):

    def get_queryset(self):
        recently_viewed_companies = CompanyRecentlyViewed.objects.filter(user_object = self.request.user).order_by('-timestamp')
        recently_viewed_company_ids = [viewed_company.company_object_id for viewed_company in recently_viewed_companies]        
        companies = Company.objects.filter(pk__in=recently_viewed_company_ids)
        return companies
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recently_viewed'] = True
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
            "billing_address" : organization.billing_address,
            "billing_city" : organization.billing_city,
            "billing_state" : organization.billing_state,
            "billing_postal_code" : organization.billing_postal_code,
            "billing_country" : organization.billing_country,
            "shipping_address" : organization.shipping_address,
            "shipping_city" : organization.shipping_city,
            "shipping_state" : organization.shipping_state,
            "shipping_postal_code" : organization.shipping_postal_code,
            "shipping_country" : organization.shipping_country,
            "date_to_remember" : organization.date_to_remember,
            "description" : organization.description,
            "tag_list" : organization.tag_list,
            "permission" : organization.permission,            
            "created": organization.created.strftime("%d/%m/%Y"),
            "updated": organization.updated.strftime("%d/%m/%Y")
        }
        if organization.record_owner:
            serialized_data["record_owner"] = organization.record_owner.id,

        if organization.image:
            serialized_data["image"] = organization.image.url

        if organization.billing_address and organization.billing_city and organization.billing_state and organization.billing_postal_code and organization.billing_country:
            full_billing_address = f"{organization.billing_address}, {organization.billing_city}, {organization.billing_state}, {organization.billing_postal_code}, {organization.billing_country}."
            serialized_data["full_billing_address"] = full_billing_address        

        if organization.shipping_address and organization.shipping_city and organization.shipping_state and organization.shipping_postal_code and organization.shipping_country :            
            full_shipping_address = f"{organization.shipping_address}, {organization.shipping_city}, {organization.shipping_state}, {organization.shipping_postal_code}, {organization.shipping_country}."
            serialized_data["full_shipping_address"] = full_shipping_address

        return JsonResponse(serialized_data)

class UpdateOrganizationView(BaseOrganizationView, UpdateView):    
    fields="__all__"
    pk_url_kwarg = 'pk'
    context_object_name = "organization"
    success_url = reverse_lazy('organizations:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Company Updated.")
        return response
    
class ChangeOrganizationImageView(BaseOrganizationView, UpdateView):
    model = Company
    fields = ["image"]
    success_url = reverse_lazy('organizations:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Company image updated.")
        return response


class ChangeOrganizationRecordOwnerView(BaseOrganizationView, UpdateView):
    model = Company
    fields = ["record_owner"]
    success_url = reverse_lazy('organizations:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = self.get_object()
        print(self.object.record_owner)
        messages.success(self.request, "Organization record owner updated successfully.")
        return response


class DeleteOrganizationView(BaseOrganizationView, View):    
    model = Company
    pk_url_kwarg = 'pk'
    context_object_name = 'organization'
    success_url = reverse_lazy('organizations:list')

    def get(self, request, *args, **kwargs):
        try:
            self.object = get_object_or_404(Company, pk = self.kwargs['pk'])
            self.object.delete()        
            messages.success(self.request, "Organization deletion successfull.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(self.request, "Cannot delete this item because it is referenced by other objects.")
            return redirect(reverse_lazy('organizations:list'))
