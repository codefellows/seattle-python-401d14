# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

# Create your views here.

class HomePageView(TemplateView):
    # Define the template
    template_name = 'home.html'

class SnacksPageView(ListView):
    template_name = 'snacks.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack

#1. Create the view
#2. Add a url
#3. Create an html page