from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, PipelineStage
from django.contrib import messages
from django.http import Http404

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
    

class ProjectCloneView(BaseProjectView, CreateView):
    model = Project
    success_url = reverse_lazy('projects:list')

    def get_object(self, **kwargs):
        try:
            return get_object_or_404(Project, pk = self.kwargs['pk'])            
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        try:
            project = Project.objects.create(
                image = self.object.image,
                name = self.object.name,
                status = self.object.status,
                category = self.object.category,
                user_responsible = self.object.user_responsible,
                pipeline = self.object.pipeline,                
                description = self.object.description,
                tag_list = self.object.tag_list,
                visibility = self.object.visibility
            )

            stages = [stage.id for stage in self.object.stage.all()]
            project.stage.add(*stages)
            project.save()
            messages.success(self.request, "Cloned project successfully.")
            return redirect(self.get_success_url())
        except Exception as e:
            print(e)
            return redirect(reverse_lazy('authentication:error500'))


class ProjectUpdateView(BaseProjectView, UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy('projects:list')

    def form_valid(self, form):
        messages.success(self.request, "Project updated successfully.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Project updation failed.")
        for field, errors in form.fields.items():
            for error in errors:
                print(f"Error on field {field}: {error}")
        return redirect(reverse_lazy('projects:list'))


class ProjectImageUpdateView(BaseProjectView, UpdateView):
    model = Project
    fields = ["image"]
    success_url = reverse_lazy('projects:list')

    def form_valid(self, form):
        messages.success(self.request, "Project image updated successfully.")
        return super().form_valid(form)


class ProjectOwnerUpdateView(BaseProjectView, UpdateView):
    model = Project
    fields = ["record_owner"]
    success_url = reverse_lazy('projects:list')

    def form_valid(self, form):
        messages.success(self.request, "Project owner updated successfully.")
        return super().form_valid(form)


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
            if field_name not in ("user_responsible", "stage", "created", "updated", "image"):
                field_value = getattr(project, field_name)
                serialized_data[field_name] = field_value
            
        serialized_data.update({                        
            "created": project.created.strftime("%d/%m/%Y"),
            "updated": project.updated.strftime("%d/%m/%Y")
        })        

        if project.image:
            serialized_data['image'] = project.image.url

        if project.stage:
            serialized_data.update({
                "stage" : [stage.stage for stage in project.stage.all()],
                "stage_id" : [stage.id for stage in project.stage.all()],
                })

        if project.user_responsible:
            serialized_data.update({
                "user_responsible": project.user_responsible.name,
                "user_responsible_id": project.user_responsible.pk,
            })

        if project.record_owner:
            serialized_data.update({
                "record_owner": project.record_owner.name,
                "record_owner_id": project.record_owner.pk,
            })

        latest_stage = project.stage.latest('-stage').stage if project.stage.exists() else None        
        serialized_data["deal_state"] = latest_stage

        return JsonResponse(serialized_data)

class ProjectStageUpdateView(BaseProjectView, UpdateView):
    fields = ["stage"]
    success_url = reverse_lazy("projects:list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()        
        
        update_stage = self.request.POST.getlist("update_stage") 
        self.object.stage.clear()
        self.object.stage.add(*update_stage)

        return redirect(self.get_success_url())

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Pipeline Stage Updation Successfull')
        print("Pipeline Stage Updation Successfull")
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)        
        for field, errors in form.fields.items():
            for error in errors:
                print(f"Error in {field}: {error}")
        return response    
    


class ProjectDeleteView(BaseProjectView, View):
    model: Project
    success_url = reverse_lazy('projects:list')

    def get(self, request, *args, **kwargs):
        try: 
            self.object = get_object_or_404(Project, pk = self.kwargs['pk'])
            try:
                self.object.delete()
                messages.success(self.request, "Project deletion successfull.")
                return redirect(self.success_url)
            except Exception as e:
                print(e)
                return redirect(reverse_lazy('authentication:error500'))
        except Http404:
            return redirect(reverse_lazy('authentication:error404'))
