from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Table
# Create your views here.

class TableListView(ListView):
    model = Table
    template_name = 'tables/table_list.html'