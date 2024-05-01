from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, IngredientUpdateForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


# READ VIEWS
class HomePageView(TemplateView):
    template_name = 'home.html'


class InventoryPageView(ListView):
    template_name = 'pages/inventory.html'
    model = Ingredient
    ordering = "name"


def menu_items_page(request):
    menu_items = MenuItem.objects.all()
    recipe_requirements = RecipeRequirement.objects.all()

    return render(request, "pages/menu.html", {"menu_items": menu_items, "recipe_requirements": recipe_requirements})


def revenue_and_profits_page(request):
    purchased_items = Purchase.objects.all()
    all_sales = [p.menu_item.price for p in purchased_items]
    total_revenue = sum(all_sales)


class PurchasesPageView(ListView):
    template_name = 'pages/purchases.html'
    model = Purchase


# CREATE VIEWS
class CreateInventoryView(CreateView):
    model = Ingredient
    template_name = 'pages/inventory_create.html'
    form_class = IngredientForm
    success_url = reverse_lazy('inventory')


class MenuItemCreate(CreateView):
    template_name = 'pages/menu_create.html'
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy('menu')


def purchase_create_page(request):
    # TODO: add logic to update ingredient QTYs in inventory when new purchase is made
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('purchases'))
    else:
        form = PurchaseForm()

    menu_items = MenuItem.objects.all()
    required_recipes = RecipeRequirement.objects.all()
    inventory = Ingredient.objects.all()

    context = {
        "form": form,
        "menu_items": menu_items,
        "required_recipes": required_recipes,
        "inventory": inventory,
    }

    return render(request, 'pages/purchases_create.html', context)


def recipe_requirement_create_page(request):
    if request.method == 'POST':
        form = RecipeRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('menu'))
    else:
        form = RecipeRequirementForm()

    menu_items = MenuItem.objects.all()
    ingredients = Ingredient.objects.all()

    context = {
        "form": form,
        "menu_items": menu_items,
        "ingredients": ingredients,
    }

    return render(request, "pages/menu_add_ingredient.html", context)


# UPDATE VIEWS
class UpdateInventoryView(UpdateView):
    template_name = 'pages/inventory_update.html'
    model = Ingredient
    form_class = IngredientUpdateForm
    success_url = reverse_lazy('inventory')


# DELETE VIEWS
class DeleteInventoryView(DeleteView):
    model = Ingredient
    template_name = 'pages/inventory_delete.html'
    success_url = reverse_lazy('inventory')
