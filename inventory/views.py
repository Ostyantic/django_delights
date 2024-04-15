from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase


class HomePageView(TemplateView):
    template_name = 'home.html'


class InventoryPageView(ListView):
    template_name = 'pages/inventory.html'
    model = Ingredient


class MenuItemsPageView(ListView):
    template_name = 'pages/menu.html'
    model = RecipeRequirement


class PurchasesPageView(ListView):
    template_name = 'pages/purchases.html'
    model = Purchase
