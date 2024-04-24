from django import forms

from .models import Ingredient, Purchase, MenuItem, RecipeRequirement


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
