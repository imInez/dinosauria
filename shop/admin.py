from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'available']
    list_filter = ['available']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ('name',)}
