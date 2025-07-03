import pytest
from customers.models import Customer
from sales.models import Sale
from datetime import date, timedelta
from decimal import Decimal
from django.db import models
from model_bakery import baker

@pytest.mark.django_db
def test_highest_sales_volume():
    c1 = baker.make(Customer)
    c2 = baker.make(Customer)
    Sale.objects.create(customer=c1, amount=100, sale_date=date.today())
    Sale.objects.create(customer=c1, amount=200, sale_date=date.today())
    Sale.objects.create(customer=c2, amount=50, sale_date=date.today())
    top = Customer.objects.annotate(total_sales=models.Sum('sales__amount')).order_by('-total_sales').first()
    assert top == c1

@pytest.mark.django_db
def test_highest_average_sale():
    c1 = baker.make(Customer)
    c2 = baker.make(Customer)
    Sale.objects.create(customer=c1, amount=100, sale_date=date.today())
    Sale.objects.create(customer=c2, amount=200, sale_date=date.today())
    Sale.objects.create(customer=c2, amount=100, sale_date=date.today())
    top = Customer.objects.annotate(avg_sale=models.Avg('sales__amount')).order_by('-avg_sale').first()
    assert top == c2

@pytest.mark.django_db
def test_highest_purchase_frequency():
    c1 = baker.make(Customer)
    c2 = baker.make(Customer)
    Sale.objects.create(customer=c1, amount=100, sale_date=date.today())
    Sale.objects.create(customer=c1, amount=200, sale_date=date.today() - timedelta(days=1))
    Sale.objects.create(customer=c2, amount=50, sale_date=date.today())
    top = Customer.objects.annotate(unique_days=models.Count('sales__sale_date', distinct=True)).order_by('-unique_days').first()
    assert top == c1 