import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from sales.models import Sale
from datetime import date, timedelta

@pytest.mark.django_db
def test_sales_statistics():
    client = APIClient()
    user = baker.make('customers.Customer', password='12345678')
    client.force_authenticate(user=user)
    # Cria vendas em dias diferentes
    for i in range(3):
        Sale.objects.create(customer=user, amount=100*(i+1), sale_date=date.today() - timedelta(days=i))
    response = client.get('/api/sales/statistics/')
    assert response.status_code == 200
    assert 'daily_sales' in response.data
    assert len(response.data['daily_sales']) >= 1

@pytest.mark.django_db
def test_customer_statistics():
    client = APIClient()
    user = baker.make('customers.Customer', password='12345678')
    client.force_authenticate(user=user)
    # Cria vendas para múltiplos clientes
    c1 = baker.make('customers.Customer', full_name='Ana')
    c2 = baker.make('customers.Customer', full_name='Carlos')
    Sale.objects.create(customer=c1, amount=200, sale_date=date.today())
    Sale.objects.create(customer=c1, amount=100, sale_date=date.today())
    Sale.objects.create(customer=c2, amount=50, sale_date=date.today())
    response = client.get('/api/sales/customers/statistics/')
    assert response.status_code == 200
    assert 'highest_volume' in response.data
    assert 'highest_average' in response.data
    assert 'highest_frequency' in response.data 