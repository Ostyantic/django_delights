from django.urls import path

from .views import HomePageView, InventoryPageView, MenuItemsPageView, PurchasesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('menu/', MenuItemsPageView.as_view(), name="menu"),
    path('purchases/', PurchasesPageView.as_view(), name="purchases"),
]