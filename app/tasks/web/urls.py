from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", login_required(TaskCreateView.as_view(), login_url="login"), name="task_create"),
    path("tasks/<str:pk>/", login_required(TaskDetailView.as_view(), login_url="login"), name="task_detail"),
    path("tasks/<str:pk>/update/", login_required(TaskUpdateView.as_view(), login_url="login"), name="task_update"),
    path("tasks/<str:pk>/delete/", login_required(TaskDeleteView.as_view(), login_url="login"), name="task_delete"),
]
