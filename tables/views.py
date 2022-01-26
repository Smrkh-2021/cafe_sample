from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Table
# Create your views here.

class TableListView(ListView):
    model = Table
    template_name = 'tables/table_list.html'

class TableUpdateView(UpdateView):
    model = Table
    fields = '__all__'
    template_name_suffix = '_update_form'