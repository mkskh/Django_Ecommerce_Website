from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total_item_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.product} x {self.quantity}"
