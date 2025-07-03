from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Sale(models.Model):
    """
    Model representing a sale transaction in the toy store.
    
    Attributes:
        customer: Reference to the customer who made the purchase
        amount: Sale amount in decimal format
        sale_date: Date when the sale occurred
        created_at: Timestamp when sale record was created
    """
    
    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
        related_name='sales',
        verbose_name="Cliente"
    )
    
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Valor da venda"
    )
    
    sale_date = models.DateField(
        verbose_name="Data da venda"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-sale_date', '-created_at']
        indexes = [
            models.Index(fields=['sale_date']),
            models.Index(fields=['customer', 'sale_date']),
        ]

    def __str__(self):
        return f"Venda #{self.id} - {self.customer.full_name} - R$ {self.amount}"