from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import TemplateView, CreateView, DetailView
from leads.models import Lead
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.core.serializers import serialize

from .models import Program, Course

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

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        program = request.POST.get('program')
        program = Program.objects.filter(pk = program).first().name
        course = request.POST.get('course')
        course = Course.objects.filter(pk = course).first().name

        try:
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                description = f"Interested in {program} in {course} at  {city}, {state}."            
            )
            messages.success(self.request, "Registration successfull.")
            return redirect(self.success_url)
        except Exception as e:
            print(e)
            return redirect(reverse_lazy('authentication:error500'))


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

    def get(self, request, *args, **kwargs):
        data = request.GET

        state = data.get('state')
        city = data.get('city')

        programs = Program.objects.filter(state__name=state, district__name=city).values_list('id', 'name')
        return JsonResponse(list(programs), safe=False)
    

class GetCourseView(DetailView):
    model = Course

    def get(self, request, *args, **kwargs):
        data = request.GET

        state = data.get('state')
        city = data.get('city')
        program = data.get('program')
        
        print(state)
        print(city)
        print(program)

        courses = Course.objects.filter(state__name=state, district__name=city, program = program).values_list('id', 'name')        

        if courses:
            print(len(courses))
    
        return JsonResponse(list(courses), safe=False)