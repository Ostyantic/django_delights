from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('inventory/', views.InventoryPageView.as_view(), name="inventory"),
    path('inventory/add', views.CreateInventoryView.as_view(), name="add_inventory"),
    path('menu/', views.menu_items_page, name="menu"),
    path('menu/add,', views.MenuItemCreate.as_view(), name='add_menu'),
    path('menu/add_menu_ingredient', views.RecipeRequirementCreate.as_view(), name='add_menu_ingredient'),
    path('purchases/', views.PurchasesPageView.as_view(), name="purchases"),
]
