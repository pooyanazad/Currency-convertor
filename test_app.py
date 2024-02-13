import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_currency_converter_api(client):
    # Simulate a POST request to the currency converter endpoint
    data = {'amount': '10', 'from_currency': 'USD', 'to_currency': 'EUR'}
    response = client.post('/', data=data)

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the response contains the expected data
    assert b'Converted Amount:' in response.data
    assert b'USD =' in response.data
    assert b'EUR' in response.data
