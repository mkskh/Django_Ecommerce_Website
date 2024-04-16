from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_details, name='cart_details'),
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("add/unknown_user", views.add_to_cart_unknown_user, name="add_to_cart_unknown_user"),
    path("update/<int:cart_item_id>/", views.update_cart_item, name="update_cart_item"),
    path("checkout/", views.checkout, name="checkout"),
    path("payment-completed/<int:order_id>/", views.payment_completed, name="payment-completed"),
]