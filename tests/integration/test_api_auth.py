import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
@pytest.mark.parametrize('url', [
    '/api/customers/',
    '/api/sales/statistics/',
    '/api/sales/customers/statistics/',
])
def test_auth_required(url):
    client = APIClient()
    response = client.get(url)
    assert response.status_code == 401 or response.status_code == 403 