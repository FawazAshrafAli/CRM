from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, PipelineStage
from django.contrib import messages
from authentication.models import CrmUser
from django.http import JsonResponse
from organizations.models import Company
from deals.models import Deal
from contacts.models import Contact

class BaseProjectView(LoginRequiredMixin):
    login_url = 'authentication:login'
    model = Project
    template_name = "projects/projects.html"


class ProjectCreateView(BaseProjectView, CreateView):    
    fields = "__all__"
    success_url = reverse_lazy("projects:list")

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        stage = self.request.POST.getlist('stage')
        self.object.stage.add(*stage)
        self.object.save()

        return response

    def form_valid(self, form):
        response = super().form_valid(form)                
        messages.success(self.request, "Created new project.")
        return response
    
    def form_invalid(self, form):
        super().form_invalid(form)
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error on {field}: {error}")
        messages.error(self.request, "Project creation failed.")
        return reverse_lazy('projects:list')


class ProjectListView(BaseProjectView, ListView):    
    queryset = Project.objects.all()
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update({
            "users": CrmUser.objects.all(),
            "stages": PipelineStage.objects.all(),
            "organizations" : Company.objects.all(),
            "deals": Deal.objects.all(),
            "contacts": Contact.objects.all(),
        })
        return context


class ProjectDetailView(BaseProjectView, DetailView):
    
    def render_to_response(self, context, **response_kwargs):
        project = context['object']        
        serialized_data = {}

        for field in project._meta.fields:
            field_name = field.name
            if field_name not in ("user_responsible", "stage", "created", "updated"):
                field_value = getattr(project, field_name)
                serialized_data[field_name] = field_value
            
        serialized_data.update({
            "stage": [stage.stage for stage in project.stage.all()],
            "deal_state": project.stage.latest('-stage').stage,
            "user_responsible": project.user_responsible.name,
            "created": project.created.strftime("%d/%m/%Y"),
            "updated": project.updated.strftime("%d/%m/%Y")
        })
                

        return JsonResponse(serialized_data)
    