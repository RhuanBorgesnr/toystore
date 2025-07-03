from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'amount', 'sale_date', 'created_at')
    search_fields = ('customer__full_name',)
    list_filter = ('sale_date', 'created_at')
