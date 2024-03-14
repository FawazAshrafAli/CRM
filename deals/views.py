from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.http import Http404
from .models import Deal
from authentication.models import CrmUser
from organizations.models import Company


class BaseDealView(LoginRequiredMixin):
    login_url = 'login'
    model = Deal


class CreateDealView(BaseDealView, CreateView):
    template_name = "deals/deals.html"
    success_url = reverse_lazy('deals:list')
    fields = "__all__"

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
    template_name = "deals/update.html"
    success_url = reverse_lazy("deals:detail")

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(self.request, 'Invalid deal.')
            return reverse_lazy('list_deals')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Deal Created.')
        return response
    

class ListDealView(BaseDealView, ListView):
    template_name = "deals/deals.html"
    queryset = Deal.objects.all()
    context_object_name = 'deals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'users': CrmUser.objects.all(),
            'organizations': Company.objects.all()
            })
        return context


class DetailDealView(BaseDealView, DetailView):
    template_name = "deals/detail.html"
    context_object_name = 'deal'
    pk_url_kwarg = 'pk'


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
            return reverse_lazy('list_deal')
        
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Deal deleted successfully!')
        return response