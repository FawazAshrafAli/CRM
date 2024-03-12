from django.shortcuts import render, redirect
from django.views.generic  import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.http import JsonResponse

class BaseTaskView(LoginRequiredMixin):
    model = Task
    login_url = 'authentication:login'

class TaskCreateView(BaseTaskView, CreateView):
    template_name = 'tasks/tasks.html'    
    fields=["name", "assigned_to", "category", "due_date", "start_date", "reminder_date", "progress", "priority", "status", "related_to", "description", "permission"]
    success_url = reverse_lazy('tasks:list')
    raise_exception = True

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request,"New task created")
        return response
    
    def form_invalid(self, form):
        # Iterate through form errors and add them as messages
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error in {field}: {error}")

        messages.error(self.request, "Failed to create task.")
        return super().form_invalid(form)
    
    


class TaskUpdateView(BaseTaskView, UpdateView):
    template_name = 'tasks/update.html'
    fields='__all__'
    query_pk_and_slug = 'pk'    

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        due_date = obj.due_date        
        context.update({"due_date": str(due_date)})
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task updation successfull.')
        return response

    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={'pk': self.object.pk})


class TaskListView(BaseTaskView, ListView):
    template_name = 'tasks/tasks.html'
    queryset = Task.objects.all()
    context_object_name = 'tasks'



class TaskDetailView(BaseTaskView, DetailView):
    template_name = 'tasks/detail.html'
    query_pk_and_slug = 'pk'

    def render_to_response(self, context, **response_kwargs):
        task = context['object']

        serialized_data = {
            'name': task.name,
            'assigned_to' : task.assigned_to,
            'category' : task.category,
            'due_date' : task.due_date,
            'start_date': task.start_date,
            'reminder_date': task.reminder_date,
            'progress': task.progress,
            'priority': task.priority,
            'status' : task.status,
            'related_to' : task.related_to,
            'description': task.description,
            'permission': task.permission
        }

        return JsonResponse(serialized_data)

class TaskDeleteView(BaseTaskView, DeleteView):
    template_name = 'tasks/confirm_deletion.html'
    query_pk_and_slug = 'pk'
    success_url = reverse_lazy('tasks:list')
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse_lazy('tasks:list'))

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Task deletion successful.")
        return response
    