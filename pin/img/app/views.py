from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Test
from .forms import TestForm

class MainView(ListView):
    template_name = "main.html"
    context_object_name = 'test'
    model = Test

class CreateUser(CreateView):
    form_class = TestForm
    success_url = reverse_lazy("main")
    template_name = 'reg.html'