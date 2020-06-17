from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Snack

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ['name','description']

class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ['name','purchaser','description']

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy('snack_list')
