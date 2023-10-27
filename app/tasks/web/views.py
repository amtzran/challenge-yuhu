from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..models import Task
from .forms import TaskForm


class BaseView(View):
    """
    Base view for generic actions
    """

    model = Task
    success_url = reverse_lazy("task_list")


class TaskListView(BaseView, ListView):
    template_name = "index.html"
    context_object_name = "tasks"


class TaskDetailView(BaseView, DetailView):
    template_name = "detail.html"


class TaskCreateView(BaseView, CreateView):
    form_class = TaskForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(BaseView, UpdateView):
    form_class = TaskForm
    template_name = "form.html"


class TaskDeleteView(BaseView, DeleteView):
    template_name = "delete.html"
