from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import  reverse_lazy
from django.contrib import messages
from django.http import Http404, JsonResponse
from .models import PipelineStage

from .models import Deal
from authentication.models import CrmUser
from organizations.models import Company
from contacts.models import Contact
from projects.models import Project
from leads.models import Lead

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
    

class CloneDealView(BaseDealView, CreateView):
    modal = Deal
    fiedls = "__all__"
    success_url = reverse_lazy('deals:list')

    def get_object(self, **kwargs):
        try:
            return get_object_or_404(Deal, pk = self.kwargs['pk'])
        except Http404:
            return redirect(reverse_lazy('authentication:error'))
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            new_deal = Deal.objects.create(
                image = self.object.image,
                name = self.object.name,
                company = self.object.company,
                category = self.object.category,
                probability_of_winning = self.object.probability_of_winning,
                forecast_close_date = self.object.forecast_close_date,
                actual_close_date = self.object.actual_close_date,
                user_responsible = self.object.user_responsible,
                deal_value = self.object.deal_value,
                bid_amount = self.object.bid_amount,
                bid_type = self.object.bid_type,
                description = self.object.description,
                tag_list = self.object.tag_list,
                pipeline = self.object.pipeline,                
                visibility = self.object.visibility,                
            )
            stage = [deal_stage.pk for deal_stage in self.object.stage.all()]
            new_deal.stage.add(*stage)
            new_deal.save()
            messages.success(self.request, "Cloned deal successfully.")
            return redirect(self.get_success_url())
        
        except Exception as e:
            print(e)
            return redirect(reverse_lazy('authentication:error500'))


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
        messages.error(self.request, "Error. Deal updation failed.")
        return super().form_invalid(form)


class UpdateDealImageView(BaseDealView, UpdateView):
    model = Deal    
    success_url = reverse_lazy("deals:list")
    fields = ["image"]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Changed Deal image successfully.')
        return response
    

class UpdateDealOwnerView(BaseDealView, UpdateView):
    model = Deal    
    success_url = reverse_lazy("deals:list")
    fields = ["record_owner"]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Changed Deal owner successfully.')
        return response


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
            'prefix' : deal.prefix,         
            'first_name' : deal.first_name,
            'last_name' : deal.last_name,            
            'company' : deal.company.name,
            'company_id': deal.company.id,
            'company_title' : deal.company.title,
            'title': deal.title,
            'email': deal.email,
            'email_opted_out' : deal.email_opted_out,
            'phone' : deal.phone,
            'mobile_phone' : deal.mobile_phone,
            'fax' : deal.fax,
            'website' : deal.website,
            'industry' : deal.industry,
            'number_of_employees' : deal.number_of_employees,
            'company_phone' : deal.company.phone,
            'company_email' : deal.company.email_domains,           
            'category' : deal.category,
            'probability_of_winning' : deal.probability_of_winning,
            'forecast_close_date' : deal.forecast_close_date,
            'actual_close_date' : deal.actual_close_date,        
            'deal_value' : deal.deal_value,
            'bid_amount' : deal.bid_amount,
            'bid_type' : deal.bid_type,
            'mailing_address': deal.mailing_address,
            'mailing_city' : deal.mailing_city,
            'mailing_state' : deal.mailing_state,
            'mailing_postal_code' : deal.mailing_postal_code,
            'mailing_country' : deal.mailing_country,
            'description' : deal.description,
            'tag_list' : deal.tag_list,
            'pipeline' : deal.pipeline,
            'stages' :  [deal_stage.stage for deal_stage in deal.stage.all()],
            'stages_id' :  [deal_stage.id for deal_stage in deal.stage.all()],
            'deal_state' : deal.stage.last().stage,
            'visibility' : deal.visibility,                       
            'created' : deal.created,
            'updated' : deal.updated
        }
        if deal.image:
            serialized_data['image'] = deal.image.url,

        if deal.last_name:
            serialized_data['full_name'] = f"{deal.first_name} {deal.last_name}"
        else:
            serialized_data['full_name'] = deal.first_name

        if deal.record_owner:
            serialized_data['record_owner'] = deal.record_owner.name

        if deal.image:
            serialized_data['image'] = deal.image.url

        if deal.user_responsible:
            serialized_data.update({
                'user_responsible': deal.user_responsible.name,
                'user_responsible_id': deal.user_responsible.id,
                })
            
        if deal.record_owner:
            serialized_data['record_owner_id'] = deal.record_owner.id

        return JsonResponse(serialized_data)

class DeleteDealView(BaseDealView, View):
    model = Deal    
    pk_url_kwarg = 'pk'    
    success_url = reverse_lazy('deals:list')    
        
    def get(self, request, *args, **kwargs):
        try:
            self.object = get_object_or_404(Deal, pk = self.kwargs['pk'])
            try:
                self.object.delete()
                messages.success(self.request, "Deal deletion successfull.")
                return redirect(self.success_url)
            except Exception as e:
                print(e)
                return redirect(reverse_lazy('authentication:error500'))
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))


class DealToLeadView(BaseDealView, CreateView):
    model = Deal
    fields = "__all__"
    success_url = reverse_lazy('deals:list')

    def get_object(self, **kwargs):
        try:
            return get_object_or_404(Deal, pk = self.kwargs['pk'])
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()        
        try:
            lead = get_object_or_404(Lead,
                                     prefix = self.object.prefix,                                     
                                    first_name = self.object.first_name,
                                    last_name = self.object.last_name,                                    
                                    organization = self.object.company,
                                    email = self.object.email,
                                    phone = self.object.phone,
                                    )
            lead.archived = False
            lead.save()
            self.object.delete()
            messages.success(self.request, "Successfully changed deal to lead.")
            return redirect(self.get_success_url())
        except Http404:
            try:
                lead = Lead.objects.create(
                    image = self.object.image,
                    prefix = self.object.prefix,
                    first_name = self.object.first_name,
                    last_name = self.object.last_name,
                    organization = self.object.company,
                    title = self.object.title,
                    user_responsible = self.object.user_responsible,
                    lead_owner = self.object.record_owner,
                    email = self.object.email,
                    email_opted_out = self.object.email_opted_out,
                    phone = self.object.phone,
                    mobile_phone = self.object.mobile_phone,
                    fax = self.object.fax,
                    website = self.object.website,
                    industry = self.object.industry,
                    number_of_employees = self.object.number_of_employees,
                    mailing_address = self.object.mailing_address,
                    mailing_city = self.object.mailing_city,
                    mailing_state = self.object.mailing_state,
                    mailing_postal_code = self.object.mailing_postal_code,
                    mailing_country = self.object.mailing_country,
                    description = self.object.description,
                    tag_list = self.object.tag_list,                    
                )   

                self.object.delete()
                messages.success(self.request, "Successfully changed deal to lead.")                                    
                return redirect(self.get_success_url())
            except Exception as e:
                print(e)
                return redirect(reverse_lazy('authentication:error500'))