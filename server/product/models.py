from html.parser import attrfind_tolerant
from unicodedata import category

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "product_categories"
        verbose_name = "product category"
        verbose_name_plural = "product categories"

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='product')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    specs = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = "store_products"

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_variant')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    attributes = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        db_table = "product_variants"

    def __str__(self):
        attributes_string = ' '.join(value for value in self.attributes.values())


        return f"{self.product} - {attributes_string}"