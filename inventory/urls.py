from django.urls import path

from .views import HomePageView, InventoryPageView, CreateInventoryView, PurchasesPageView, menu_items_page

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('inventory/add', CreateInventoryView.as_view(), name="add_inventory"),
    path('menu/', menu_items_page, name="menu"),
    path('purchases/', PurchasesPageView.as_view(), name="purchases"),
]