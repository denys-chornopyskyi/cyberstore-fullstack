from django.contrib import admin
from .models import ProductCategory, Product, ProductVariant

models = [Product, ProductVariant, ProductCategory]

admin.site.register(models)

