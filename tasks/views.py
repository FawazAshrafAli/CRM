from django.shortcuts import render, redirect
from django.views.generic  import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime
from django.http import Http404
from .forms import ContactCreationForm, ContactUpdationForm

class BaseTaskView(LoginRequiredMixin):
    model = Task
    login_url = 'login'

class CreateTaskView(BaseTaskView, CreateView):
    template_name = 'tasks/create.html'    
    # fields='__all__'
    form_class = ContactCreationForm
    success_url = reverse_lazy('create_task')

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request,"New task created")
        return response


class UpdateTaskView(BaseTaskView, UpdateView):
    template_name = 'tasks/update.html'
    form_class = ContactUpdationForm    
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
        return reverse_lazy('detail_task', kwargs={'pk': self.object.pk})


class ListTaskView(BaseTaskView, ListView):
    template_name = 'tasks/tasks.html'
    queryset = Task.objects.all()
    context_object_name = 'tasks'


class DetailTaskView(BaseTaskView, DetailView):
    template_name = 'tasks/detail.html'
    query_pk_and_slug = 'pk'


class DeleteTaskView(BaseTaskView, DeleteView):
    template_name = 'tasks/confirm_deletion.html'
    query_pk_and_slug = 'pk'
    success_url = reverse_lazy('list_tasks')
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse_lazy('list_tasks'))

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Task deletion successful.")
        return response
    