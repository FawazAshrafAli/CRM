from django.urls import path
from .views import (TaskCreateView, CloneTaskView, TaskUpdateView, 
                    TaskListView, TaskDetailView, TaskDeleteView, 
                    TaskOwnerUpdateView, TaskCompletionView, 
                    TaskCompletionAndCloningView, CompletedTaskListView)

app_name = "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('list_completed/', CompletedTaskListView.as_view(), name='list_completed'),
    path('update/<pk>', TaskUpdateView.as_view(), name='update'),
    path('update_task_owner/<pk>', TaskOwnerUpdateView.as_view(), name='update_task_owner'),
    path('complete/<pk>', TaskCompletionView.as_view(), name='complete'),
    path('complete_and_clone/<pk>', TaskCompletionAndCloningView.as_view(), name='complete_and_clone'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('clone/<pk>', CloneTaskView.as_view(), name='clone'),
    path('detail/<pk>', TaskDetailView.as_view(), name='detail'),
    path('delete/<pk>', TaskDeleteView.as_view(), name='delete'),
]
