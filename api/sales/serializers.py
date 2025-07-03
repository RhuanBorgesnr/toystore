from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'customer', 'amount', 'sale_date', 'created_at']
        read_only_fields = ['id', 'created_at']
