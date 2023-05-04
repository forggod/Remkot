from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from .forms import *
from .models import *


def index(request):
    return render(request, 'index.html')


class Table(ListView):
    model = ServiceApplication
    template_name = 'table.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявки'
        return context

    def get_queryset(self):
        return ServiceApplication.objects


class AddClient(CreateView):
    form_class = AddClientForm
    template_name = 'addClient.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление клиента'
        return context
