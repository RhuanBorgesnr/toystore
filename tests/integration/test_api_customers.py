import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.mark.django_db
def test_create_customer_authenticated():
    client = APIClient()
    user = baker.make('customers.Customer', full_name='Rhuan Borges', email='rhuan@example.com', password='12345678')
    client.force_authenticate(user=user)
    data = {
        'username': 'rhuan_user',
        'full_name': 'Rhuan Borges',
        'email': 'rhuan.novo@email.com',
        'birth_date': '1990-01-01',
        'password': '12345678'
    }
    response = client.post('/api/customers/', data)
    assert response.status_code == 201
    assert response.data['full_name'] == 'Rhuan Borges'

@pytest.mark.django_db
def test_list_customers_with_filter():
    client = APIClient()
    user = baker.make('customers.Customer', full_name='Rhuan Borges', email='rhuan@example.com', password='12345678')
    baker.make('customers.Customer', full_name='Rhuana Teste', email='rhuana@x.com')
    baker.make('customers.Customer', full_name='Carlos Teste', email='carlos@x.com')
    client.force_authenticate(user=user)
    response = client.get('/api/customers/?full_name=rhuana')
    assert response.status_code == 200
    assert any('Rhuana Teste' in str(c) for c in response.data['data']['clientes'])

@pytest.mark.django_db
def test_update_customer():
    client = APIClient()
    user = baker.make('customers.Customer', full_name='Rhuan Borges', email='rhuan@example.com', password='12345678')
    client.force_authenticate(user=user)
    data = {'full_name': 'Rhuan Borges Editado'}
    response = client.patch(f'/api/customers/{user.id}/', data)
    assert response.status_code == 200
    assert response.data['full_name'] == 'Rhuan Borges Editado'

@pytest.mark.django_db
def test_delete_customer():
    client = APIClient()
    user = baker.make('customers.Customer', full_name='Rhuan Borges', email='rhuan@example.com', password='12345678')
    client.force_authenticate(user=user)
    response = client.delete(f'/api/customers/{user.id}/')
    assert response.status_code == 200 or response.status_code == 204
