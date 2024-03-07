from django.urls import path
from .views import CreateTaskView, UpdateTaskView, ListTaskView, DetailTaskView, DeleteTaskView

app_name = "tasks"

urlpatterns = [
    path('', ListTaskView.as_view(), name='list_tasks'),
    path('update_task/<pk>', UpdateTaskView.as_view(), name='update_task'),
    path('create_task/', CreateTaskView.as_view(), name='create_task'),
    path('detail_task/<pk>', DetailTaskView.as_view(), name='detail_task'),
    path('delete_task/<pk>', DeleteTaskView.as_view(), name='delete_task'),
]
