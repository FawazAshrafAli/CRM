from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from leads.models import Lead
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Program

class FormView(TemplateView):
    template_name = 'capture_form/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        states = [
            "Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh",  "Assam",  "Bihar", "Chandigarh", 
            "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Goa", "Gujarat", "Haryana", 
            "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", 
            "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", 
            "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ]
        context['states'] = states
        return context


class CreateLeadView(FormView, CreateView):
    model = Lead
    fields = ["first_name", "last_name", "email", "phone", "description"]
    success_url = reverse_lazy('capture_form:form')

    def form_valid(self, form):
        messages.success(self.request, "Registration successfull.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error at {field}: {error}")
        return super().form_invalid(form)
    

class GetProgramView(DetailView):
    model = Program

    def post(self, request, *args, **kwargs):
        data = request.POST

        state = data.get('state')
        district = data.get('district')