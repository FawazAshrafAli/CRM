from django.urls import path
from .views import TaskCreateView, CloneTaskView, TaskUpdateView, TaskListView, TaskDetailView, TaskDeleteView

app_name = "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('update/<pk>', TaskUpdateView.as_view(), name='update'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('clone/<pk>', CloneTaskView.as_view(), name='clone'),
    path('detail/<pk>', TaskDetailView.as_view(), name='detail'),
    path('delete/<pk>', TaskDeleteView.as_view(), name='delete'),
]
