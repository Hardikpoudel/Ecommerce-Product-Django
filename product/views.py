from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import products
import os
# Create your views here.


class list(ListView):
    model = products
    template_name = "home.html"


class detail(DetailView):
    model = products
    template_name = "detail.html"
