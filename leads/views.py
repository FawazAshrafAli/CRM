from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import render, redirect
from .models import Lead
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404, JsonResponse
from organizations.models import Company
from django.views.decorators.csrf import csrf_exempt
from authentication.models import CrmUser

class BaseLeadView(LoginRequiredMixin):
    model = Lead
    login_url = 'authentication:login'
    template_name = 'leads/leads.html' #

class CreateLeadView(BaseLeadView, CreateView):
    template_name = 'leads/leads.html'    
    fields = "__all__"
    success_url = reverse_lazy('leads:list')
    raise_exception = True

    def form_valid(self, form):
        messages.success(self.request, 'Created Lead successfully.')
        return super().form_valid(form)    
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Something went wrong')
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error on {field}: {error}")
        return response    

    
class ListLeadView(BaseLeadView, ListView):
    template_name = 'leads/leads.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "organizations" : Company.objects.all(),
            "users" : CrmUser.objects.all()
        })        
        return context

class DetailLeadView(BaseLeadView, DetailView):
    template_name = 'leads/detail.html'
    pk_url_kwarg = 'pk'    


    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(self.request, 'Invalid lead')
            return redirect(reverse_lazy('leads:list'))
        
    def render_to_response(self, context, **response_kwargs):
        lead = context['object']
                
        serialized_data = {
            "id" : lead.id,        
            "prefix" : lead.prefix,
            "first_name": lead.first_name,
            "last_name": lead.last_name,
            "organization" : lead.organization.id,
            "title" : lead.title,
            "lead_status" : lead.lead_status,
            "mailing_address": lead.mailing_address,
            "mailing_city": lead.mailing_city,
            "mailing_state": lead.mailing_state,
            "mailing_postal_code": lead.mailing_postal_code,
            "mailing_country": lead.mailing_country,           
            "lead_rating" : lead.lead_rating,
            "email" : lead.email,
            "email_opted_out" : lead.email_opted_out,
            "phone" : lead.phone,
            "mobile_phone" : lead.mobile_phone,
            "fax" : lead.fax,
            "website" : lead.website,
            "industry" : lead.industry,
            "number_of_employees" : lead.number_of_employees,
            "lead_source" : lead.lead_source,            
            "description" : lead.description,
            "tag_list" : lead.tag_list,
            "permission" : lead.permission,
            "created" : lead.created.strftime("%d-%b-%y %I:%M %p"),
            "updated" : lead.updated.strftime("%d/%m/%Y")
        }

        if lead.image:
            serialized_data["image"] = lead.image.url

        if lead.first_name and lead.last_name:
            serialized_data["full_name"] = f"{lead.first_name} {lead.last_name}"
        elif lead.first_name:
            serialized_data["full_name"] = lead.first_name

        if lead.user_responsible:
            serialized_data["user_responsible"] = lead.user_responsible.id,

        if lead.mailing_address and lead.mailing_city and lead.mailing_state and lead.mailing_postal_code and lead.mailing_country:
            full_mailing_address = f"{lead.mailing_address}, {lead.mailing_city}, {lead.mailing_state}, {lead.mailing_postal_code}, {lead.mailing_country}."
            serialized_data['full_mailing_address'] = full_mailing_address

        return JsonResponse(serialized_data)

class UpdateLeadView(BaseLeadView, UpdateView):    
    pk_url_kwarg = 'pk'
    fields = "__all__"
    success_url = reverse_lazy('leads:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Lead updation successfull.')
        return response
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error on  field {field}: {error}")
        return  super().form_invalid(form)
    

class UpdateLeadImageView(BaseLeadView, UpdateView):    
    pk_url_kwarg = 'pk'
    fields = ["image"]
    success_url = reverse_lazy('leads:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Successfully Changed Lead Image.')
        return response    


# For updating lead status using ajax
class UpdateLeadStatusView(BaseLeadView, UpdateView):
    template_name = 'leads/leads.html'
    pk_url_kwarg = 'pk'
    fields = ["lead_status"]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {'message': 'Error'}        
        self.object.lead_status = request.POST.get('new_status')
        self.object.save()              
        data = {'message': 'Success', 'id': self.object.id}

        return JsonResponse(data)


class DeleteLeadView(BaseLeadView, DeleteView):
    template_name = 'leads/confirm_deletion.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('leads:list')

    def get(self, request, *args , **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(self.request, 'Invalid lead')
            return redirect(reverse_lazy('leads:list'))

    def delete(self, request, *args, **kwargs):
        response =  super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Lead Deleted.')
        return response