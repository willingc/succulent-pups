# garden/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from .models import Garden

class GardenListView(ListView):
    model = Garden


class GardenDetailView(DetailView):
    model = Garden
