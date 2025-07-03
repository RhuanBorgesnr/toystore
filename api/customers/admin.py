from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'email', 'birth_date', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'full_name', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
