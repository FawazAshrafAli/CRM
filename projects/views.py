from django.shortcuts import render
from django.views.generic import  TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project

class BaseProjectView(LoginRequiredMixin):
    login_url = 'login'
    model = Project


class ProjectListView(BaseProjectView, ListView):
    template_name = "projects/projects.html"
    queryset = Project.objects.all()