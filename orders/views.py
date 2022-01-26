from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Order
# Create your views here.

class OrderListView(ListView):
    model = Order
    template_name = 'orders/list_view.html'