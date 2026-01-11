from django.db import models
from products.models import Products


class Basket(models.Model):
  item = models.ForeignKey(Products, on_delete=models.CASCADE)
  basket_quantity = models.PositiveIntegerField(default=0)
  customer_name = models.CharField(max_length=50, blank=True, null=True)
  phone = models.CharField(max_length=15, blank=True, null=True)
  adress =models.TextField(max_length=50, blank=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)



  def __str__(self):
    return f'{self.product.name_models}, {self.basket_quantity}'