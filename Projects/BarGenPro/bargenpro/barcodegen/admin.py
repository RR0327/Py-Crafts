from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_type', 'code_value', 'price')
    search_fields = ('name', 'code_value', 'code_type')
