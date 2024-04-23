"""
URL configuration for zencrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace="dashboard")), # dashboard interface
    path('authentication/', include('authentication.urls', namespace="authentication")), # User authentication and registration
    path('contacts/', include('contacts.urls', namespace="contacts")), # contact CRUD and listing
    path('organizations/', include('organizations.urls', namespace="organizations")), # organization CRUD and listing
    path('leads/', include('leads.urls', namespace="leads")),  # lead management
    path('deals/', include('deals.urls', namespace="deals")),  # deal management
    path('tasks/', include('tasks.urls', namespace="tasks")),   # task management    
    path('projects/', include('projects.urls', namespace="projects")),   # project management    
    path('activities/', include('activities.urls', namespace="activities")),   # activity management    
    path('reports/', include('reports.urls', namespace="reports")),   # activity management
    path('form/', include('capture_form.urls', namespace="capture_form")),   # form capture
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
