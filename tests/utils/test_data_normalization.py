import pytest

def normalize_customer_data(raw):
    return {
        'full_name': raw['info']['nomeCompleto'],
        'email': raw['info']['detalhes']['email'],
        'birth_date': raw['info']['detalhes']['nascimento'],
        'sales': raw['estatisticas']['vendas'],
    }

def test_normalize_customer_data():
    raw = {
        "info": {
            "nomeCompleto": "Rhuan Borges",
            "detalhes": {
                "email": "rhuan.b@example.com",
                "nascimento": "1995-08-15"
            }
        },
        "duplicado": {
            "nomeCompleto": "Rhuan Borges"
        },
        "estatisticas": {
            "vendas": [
                {"data": "2024-01-01", "valor": 200},
                {"data": "2024-01-02", "valor": 100}
            ]
        }
    }
    normalized = normalize_customer_data(raw)
    assert normalized['full_name'] == "Rhuan Borges"
    assert normalized['email'] == "rhuan.b@example.com"
    assert normalized['birth_date'] == "1995-08-15"
    assert len(normalized['sales']) == 2
