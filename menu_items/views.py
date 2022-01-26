from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from menu_items.models import MenuItem


class MenuItemsListView(ListView):
    model = MenuItem
    template_name = 'menu_items/menu_list.html'