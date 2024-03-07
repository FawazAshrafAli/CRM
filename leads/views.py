from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import render, redirect
from .models import Lead
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from .forms import LeadUpdationForm
from django.http import Http404

class BaseLeadView(LoginRequiredMixin):
    model = Lead
    login_url = 'login'

class CreateLeadView(BaseLeadView, CreateView):
    template_name = 'leads/create.html'
    # fields = ["full_name", "title", "company", "phone", "email", "lead_owner"]
    fields = "__all__"
    success_url = reverse_lazy('list_leads')
    raise_exception = True

    def form_valid(self, form):
        messages.success(self.request, 'Created Lead successfully.')
        return super().form_valid(form)    
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Something went wrong')
        return response
    


class UpdateLeadView(BaseLeadView, UpdateView):
    template_name = 'leads/update.html'
    pk_url_kwarg = 'pk'
    form_class = LeadUpdationForm

    def form_valid(self, form):
        messages.success(self.request, 'Lead updation successfull.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('detail_lead', kwargs={'pk': self.object.id})


class ListLeadView(BaseLeadView, ListView):
    template_name = 'leads/list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

class DetailLeadView(BaseLeadView, DetailView):
    template_name = 'leads/detail.html'
    pk_url_kwarg = 'pk'    


    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(self.request, 'Invalid lead')
            return redirect(reverse_lazy('list_leads'))

class DeleteLeadView(BaseLeadView, DeleteView):
    template_name = 'leads/confirm_deletion.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('list_leads')

    def get(self, request, *args , **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(self.request, 'Invalid lead')
            return redirect(reverse_lazy('list_leads'))

    def delete(self, request, *args, **kwargs):
        response =  super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Lead Deleted.')
        return response