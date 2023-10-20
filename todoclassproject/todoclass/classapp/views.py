from django.shortcuts import render

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import *

from  django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class TaskListView(ListView):
    model = TodoModel
    template_name = 'main.html'
    context_object_name = 'task'

    
class TaskDetailtView(DetailView):
    model = TodoModel
    template_name = 'show.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = TodoModel
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('classapp:show',kwargs={'pk':self.object.id})


class TaskDeletetView(DeleteView):
    model = TodoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('classapp:show')