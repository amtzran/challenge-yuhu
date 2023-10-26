from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<str:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/<str:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<str:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]
