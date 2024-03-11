from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.http import Http404
from .models import Deal


class BaseDealView(LoginRequiredMixin):
    login_url = 'login'
    model = Deal


class CreateDealView(BaseDealView, CreateView):
    template_name = "deals/create.html"
    success_url = reverse_lazy('list_deals')
    fields = ["deal_name", "company", "forecast_close_date", "user_responsible", "deal_value"]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Deal Created.')
        return response
    

class UpdateDealView(BaseDealView, UpdateView):
    template_name = "deals/update.html"
    success_url = reverse_lazy("detail_deal")

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