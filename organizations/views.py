from django.shortcuts import render
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
# from  .models import Company
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseOrganizationView(LoginRequiredMixin):
    # model = Company
    login_url = 'login'


class CreateOrganizationView(BaseOrganizationView, CreateView):    
    template_name = 'organizations/create_organization.html'
    fields="__all__"
    success_url = reverse_lazy('create_organization')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "New organization has been created!")
        return response


class ListOrganizationView(BaseOrganizationView, ListView):    
    template_name = "organizations/list_organizations.html"
    # queryset = Company.objects.all()
    context_object_name = "organizations"


class DetailOrganizationView(BaseOrganizationView, DetailView):    
    template_name = "organizations/detail_organization.html"
    query_pk_and_slug = 'pk'
    context_object_name = 'organization'


class UpdateOrganizationView(BaseOrganizationView, UpdateView):    
    template_name = "organizations/update_organization.html"
    fields="__all__"
    pk_url_kwarg = 'pk'
    context_object_name = "organization"

    def form_valid(self, form):
        response = super().form_valid(form)
        # messages.success(self.request, "Company Updated.")
        return response

    def get_success_url(self):
        return reverse_lazy('detail_organization', kwargs={'pk' : self.object.pk})    


class DeleteOrganizationView(BaseOrganizationView, DeleteView):    
    template_name = "organizations/confirm_deletion.html"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('list_organizations')
    context_object_name = 'organization'

