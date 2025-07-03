from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for Customer model with validation.
    """
    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'email', 'birth_date']
        read_only_fields = ['id']

    def validate_email(self, value):
        """
        Validate email uniqueness on update operations.
        """
        if self.instance and Customer.objects.filter(
            email=value
        ).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value

class CustomerListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
 
        sales_data = []
        for sale in instance.sales.all():
            sales_data.append({
                "data": sale.sale_date.strftime("%Y-%m-%d"),
                "valor": float(sale.amount)
            })
        
        return {
            "id": instance.id,
            "info": {
                "nomeCompleto": instance.full_name,
                "detalhes": {
                    "email": instance.email,
                    "nascimento": instance.birth_date.strftime("%Y-%m-%d")
                }
            },
            "duplicado": {
                "nomeCompleto": instance.full_name
            },
            "estatisticas": {
                "vendas": sales_data
            }
        }

    class Meta:
        model = Customer
        fields = []

class CustomerCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'full_name', 'email', 'birth_date', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = Customer.objects.create_user(
            username=validated_data['username'],
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            birth_date=validated_data['birth_date'],
            password=validated_data['password']
        )
        return user 