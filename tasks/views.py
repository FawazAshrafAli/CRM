from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic  import DeleteView, ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.http import JsonResponse

from authentication.models import CrmUser
from contacts.models import Contact
from deals.models import Deal
from projects.models import Project
from organizations.models import Company
from leads.models import Lead

class BaseTaskView(LoginRequiredMixin): #base class
    model = Task
    login_url = 'authentication:login'
    template_name = 'tasks/tasks.html'

class TaskCreateView(BaseTaskView, CreateView): # For creating task.
    fields=["name", "assigned_to", "category", "due_date", "start_date", "reminder_date", "progress", "priority", "status", "related_to", "description", "permission"]
    success_url = reverse_lazy('tasks:list')
    raise_exception = True

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request,"New task created")
        return response
    
    def form_invalid(self, form):        
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error in {field}: {error}")

        messages.error(self.request, "Failed to create task.")
        return super().form_invalid(form)


# def clone(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#         Task.objects.create(
#             name = task.name,
#             assigned_to = task.assigned_to,
#             category = task.category,
#             due_date = task.due_date,
#             start_date = task.start_date,
#             reminder_date = task.reminder_date,
#             progress = task.progress,
#             priority = task.priority,
#             status = task.status,
#             related_to = task.related_to,
#             description = task.description,
#             permission = task.permission,
#             task_owner = task.task_owner
#         )
#         return redirect('tasks:list')
#     except Task.DoesNotExist:
#         return HttpResponse("Task does not exists.")
    
class CloneTaskView(BaseTaskView, View):
    def get(self, request, pk):
        try:
            task = get_object_or_404(Task, pk=pk)
            Task.objects.create(
                name=task.name,
                assigned_to=task.assigned_to,
                category=task.category,
                due_date=task.due_date,
                start_date=task.start_date,
                reminder_date=task.reminder_date,
                progress=task.progress,
                priority=task.priority,
                status=task.status,
                related_to=task.related_to,
                description=task.description,
                permission=task.permission,
                task_owner=task.task_owner
            )
            return redirect('tasks:list')
        except Task.DoesNotExist:
            return HttpResponse("Task does not exist.")


class TaskUpdateView(BaseTaskView, UpdateView): # For updating task.
    fields='__all__'
    query_pk_and_slug = 'pk'
    success_url = reverse_lazy('tasks:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task updation successfull.')
        return response    


class TaskListView(BaseTaskView, ListView): # To list tasks.
    queryset = Task.objects.all()
    context_object_name = 'tasks'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "users": CrmUser.objects.all(),
            "contacts": Contact.objects.all(),
            "deals": Deal.objects.all(),
            "projects": Project.objects.all(),
            "organizations": Company.objects.all(),
            "leads": Lead.objects.all(),          
        })

        return context

class TaskDetailView(BaseTaskView, DetailView): # For providing a detail of a single task. 
    query_pk_and_slug = 'pk'

    def render_to_response(self, context, **response_kwargs):
        task = context['object']

        serialized_data = {
            'id': task.id,
            'name': task.name,
            'assigned_to' : task.assigned_to.name,
            'assigned_to_pk': task.assigned_to.pk,
            'category' : task.category,
            'due_date' : task.due_date,
            'start_date': task.start_date,
            'reminder_date': task.reminder_date,
            'progress': task.progress,
            'priority': task.priority,
            'status' : task.status,
            'related_to' : task.related_to,
            'description': task.description,
            'permission': task.permission,
            'created_at': task.created.strftime("%d %b %Y %I:%M %p"),
            'updated_at': task.updated.strftime("%d %b %Y %I:%M %p"),            
        }

        return JsonResponse(serialized_data)

class TaskDeleteView(BaseTaskView, DeleteView):
    query_pk_and_slug = 'pk'
    success_url = reverse_lazy('tasks:list')
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(self.get_success_url())

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Task deletion successful.")
        return response
    

# class TaskDeleteView(BaseTaskView, View):
#     def get(self, request, pk):
#         try:
#             task = get_object_or_404(Task, pk=pk)
#             task.delete()
#             messages.success(request, "Task Deleted.")
#             return redirect('tasks:list')
#         except Http404:
#             return HttpResponse("invalid object")
    