from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('inventory/', views.InventoryPageView.as_view(), name="inventory"),
    path('inventory/add', views.CreateInventoryView.as_view(), name="add_inventory"),
    path('inventory/delete/<pk>', views.DeleteInventoryView.as_view(), name="delete_inventory"),
    path('inventory/update/<pk>', views.UpdateInventoryView.as_view(), name="update_inventory"),
    path('menu/', views.menu_items_page, name="menu"),
    path('menu/add,', views.MenuItemCreate.as_view(), name='add_menu'),
    path('menu/add_menu_ingredient', views.recipe_requirement_create_page, name='add_menu_ingredient'),
    path('purchases/', views.PurchasesPageView.as_view(), name="purchases"),
    path('purchases/add', views.purchase_create_page, name="add_purchase"),
    path('purchase/delete/<pk>', views.DeletePurchaseView.as_view(), name="delete_purchase"),
    path('revenue', views.revenue_and_profits_page, name="revenue"),
]
