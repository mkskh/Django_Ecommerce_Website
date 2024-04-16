from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Product
from user.models import UserProfile


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total_item_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.product} x {self.quantity}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ship_info = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
