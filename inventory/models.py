from django.db import models


class MenuItem(models.Model):
    """
    Represents an entry off the restaurant's menu
    """
    item_name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.item_name}"


class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name}"


class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.ingredient.__str__()}"


class Purchase(models.Model):
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_purchased}, {self.menu_item.__str__()}"

