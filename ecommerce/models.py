from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"
    

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=55)
    seller = models.CharField(max_length=100, default="EXTP")
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.product_name

