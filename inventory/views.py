from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, IngredientUpdateForm, MenuItemForm, RecipeRequirementForm, PurchaseForm

from .exceptions import IngredientShortageError


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


# TODO: page should keep track of the revenue and subtract inventory costs to provide profits
def revenue_and_profits_page(request):

    # data = []
    #
    # for month in range(1,13):
    #     month_purchases = Purchase.objects.get(date_purchased__month=month)
    #     month_revenue = sum([purchase.menu_item.price for purchase in month_purchases])


    purchased_items = Purchase.objects.all()
    all_sales = [item.menu_item.price for item in purchased_items]
    total_revenue = sum(all_sales)

    context = {
        "purchased_items": purchased_items,
        "all_sales": all_sales,
        "total_revenue": total_revenue,
    }

    return render(request, 'pages/revenue_and_profits.html', context)


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

    menu_items = MenuItem.objects.all()
    inventory = Ingredient.objects.all()

    # The current inventory
    inv_dict = {ingredient.name: ingredient.quantity for ingredient in inventory}

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # making a copy of the form's menu item
                purchase = form.cleaned_data.get('menu_item')

                # getting the menu_item object
                purchased_menu_item = purchase.id

                # accessing all the required ingredients needed for the menu_item object
                purchased_item_ingredients = RecipeRequirement.objects.filter(menu_item=purchased_menu_item)

                # Dictionary of each menu item's required ingredients
                req_recipes = {recipe_object.ingredient: recipe_object.quantity for recipe_object in
                               purchased_item_ingredients}

                # for every ingredient in the required recipes dictionary, remove the ingredient qty from our inventory
                # and update the inventory quantity
                for ingredient, qty in req_recipes.items():
                    if inv_dict[ingredient.name] >= qty:
                        inv_dict[ingredient.name] -= qty
                        Ingredient.objects.filter(id=ingredient.id).update(quantity=inv_dict[ingredient.name])
                    else:
                        raise IngredientShortageError(f"There aren't enough {ingredient} to create this purchase!")
            form.save()
            return redirect(reverse_lazy('purchases'))
    else:
        form = PurchaseForm()

    context = {
        "form": form,
        "menu_items": menu_items,
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


class DeletePurchaseView(DeleteView):
    model = Purchase
    template_name = 'pages/purchases_delete.html'
    success_url = reverse_lazy('purchases')
