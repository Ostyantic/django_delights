from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class InventoryPageView(ListView):
    template_name = 'pages/inventory.html'
    model = Ingredient
    ordering = "name"


class CreateInventoryView(CreateView):
    model = Ingredient
    template_name = 'pages/inventory_create.html'
    form_class = IngredientForm
    success_url = reverse_lazy('inventory')


def menu_items_page(request):
    menu_items = MenuItem.objects.all()
    recipe_requirements = RecipeRequirement.objects.all()

    return render(request, "pages/menu.html", {"menu_items": menu_items, "recipe_requirements": recipe_requirements})


class MenuItemCreate(CreateView):
    template_name = 'pages/menu_create.html'
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy('menu')


class RecipeRequirementCreate(CreateView):
    template_name = 'pages/menu_add_ingredient.html'
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url = reverse_lazy('menu')


class PurchasesPageView(ListView):
    template_name = 'pages/purchases.html'
    model = Purchase
