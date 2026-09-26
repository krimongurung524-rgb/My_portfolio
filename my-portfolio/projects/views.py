from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
