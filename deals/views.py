from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.http import Http404, JsonResponse
from .models import PipelineStage

from .models import Deal
from authentication.models import CrmUser
from organizations.models import Company
from contacts.models import Contact
from projects.models import Project

class BaseDealView(LoginRequiredMixin):
    model = Deal
    login_url = 'authentication:login'
    template_name = "deals/deals.html"


class CreateDealView(BaseDealView, CreateView):    
    success_url = reverse_lazy('deals:list')
    fields = [
        "name","company","category","probability_of_winning","forecast_close_date",
        "actual_close_date","user_responsible","deal_value","bid_amount","bid_type",
        "description","tag_list","pipeline","visibility"
    ]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        stage = self.request.POST.getlist("stage")        
        self.object.stage.add(*stage)
        self.object.save()

        return response
        

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Deal Created.')
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error on {field}: {error}")
        return response
    

class UpdateDealView(BaseDealView, UpdateView):
    model = Deal    
    success_url = reverse_lazy("deals:list")
    fields = "__all__"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Deal updation successfull.')
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error on field {field}: {error}")
        messages.error(self.request, "Error. Lead creation failed.")
        return super().form_invalid(form)


class ListDealView(BaseDealView, ListView):
    template_name = "deals/deals.html"
    queryset = Deal.objects.all()
    context_object_name = 'deals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'users': CrmUser.objects.all(),
            'organizations': Company.objects.all(),
            'stages': PipelineStage.objects.all(),
            'contacts': Contact.objects.all(),
            'projects': Project.objects.all()
            })
        return context


class DetailDealView(BaseDealView, DetailView):
    template_name = "deals/deals.html"
    context_object_name = 'deal'
    pk_url_kwarg = 'pk'

    def render_to_response(self, context, **response_kwargs):
        deal = context['object']

        serialized_data = {
            'id' : deal.id,
            'name' : deal.name,
            'company' : deal.company.name,
            'company_id': deal.company.id,
            'company_title' : deal.company.title,            
            'company_phone' : deal.company.phone,
            'company_email' : deal.company.email_domains,           
            'category' : deal.category,
            'probability_of_winning' : deal.probability_of_winning,
            'forecast_close_date' : deal.forecast_close_date,
            'actual_close_date' : deal.actual_close_date,        
            'deal_value' : deal.deal_value,
            'bid_amount' : deal.bid_amount,
            'bid_type' : deal.bid_type,
            'description' : deal.description,
            'tag_list' : deal.tag_list,
            'pipeline' : deal.pipeline,
            'stages' :  [deal_stage.stage for deal_stage in deal.stage.all()],
            'stages_id' :  [deal_stage.id for deal_stage in deal.stage.all()],
            'visibility' : deal.visibility,
            'created' : deal.created,
            'updated' : deal.updated
        }

        if deal.user_responsible:
            serialized_data.update({
                'user_responsible': deal.user_responsible.name,
                'user_responsible_id': deal.user_responsible.id,
                })

        return JsonResponse(serialized_data)

class DeleteDealView(BaseDealView, DeleteView):
    template_name = "deals/confirm_deletion.html"
    success_url = reverse_lazy('list_deals')
    context_object_name = 'deal'
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(self.request, 'Invalid Deal.')
            return reverse_lazy('deals:list')
        
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Deal deleted successfully!')
        return response