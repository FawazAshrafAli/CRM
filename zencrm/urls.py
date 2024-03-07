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
    path('authentication/', include('authentication.urls')), # User authentication and registration
    path('contacts/', include('contacts.urls')), # contact CRUD and listing
    path('organizations/', include('organizations.urls')), # organization CRUD and listing
    path('leads/', include('leads.urls')),  # lead management
    path('deals/', include('deals.urls')),  # deal management
    path('tasks/', include('tasks.urls')),   # task management    
    path('projects/', include('projects.urls')),   # project management    
    path('activities/', include('activities.urls')),   # activity management    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
