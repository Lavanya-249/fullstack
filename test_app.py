import pytest
from app import app

@pytest.fixture
def client():
    """Flask app test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_signup_missing_data(client):
    """Test signup with missing email"""
    # This assumes you have an /api/signup route from Exp 7
    response = client.post('/api/signup', json={'password': 'test123'})
    assert response.status_code == 400
    assert 'error' in response.json

def test_protected_route_no_token(client):
    """Test protected route without token"""
    # This assumes you have an /api/protected route from Exp 7
    response = client.get('/api/protected')
    assert response.status_code == 401