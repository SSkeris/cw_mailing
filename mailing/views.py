from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from mailing.models import Mailing, Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client

    def get_success_url(self):
        return reverse('distribution:clients_list')


class MailingListView(ListView):
    """Класс для отображения списка рассылок"""
    model = Mailing


class MailingDetailView(DetailView):
    """Класс для отображения одной рассылки"""
    model = Mailing
