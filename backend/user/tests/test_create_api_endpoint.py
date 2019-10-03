import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create(**params)


@pytest.mark.django_db
def test_public_create_new_user(client):
    """Test creating a new user is successful"""
    payload = {
        'email': 'test@example.com',
        'password': 'testpass123',
        'first_name': 'Jack',
        'last_name': 'Programmer',
    }

    resp = client.post(CREATE_USER_URL, payload)

    assert resp.status_code == status.HTTP_201_CREATED
    user = get_user_model().objects.get(**resp.data)

    assert user.check_password(payload['password'])
    assert 'password' not in resp.data


@pytest.mark.django_db
def test_creating_duplicate_user_fails(client):
    """Test that creating a user that already exists fails"""
    payload = {
        'email': 'test@example.com',
        'password': 'testpass123'
    }
    create_user(**payload)

    resp = client.post(CREATE_USER_URL, payload)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    err_msg = 'user with this email already exists.'
    assert resp.json()['email'] == [err_msg]


@pytest.mark.django_db
def test_password_too_short_fails(client):
    """
    Test that creating a user that with a password less than
    8 characters fails
    """
    payload = {
        'email': 'test@example.com',
        'password': 'test123'
    }

    resp = client.post(CREATE_USER_URL, payload)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    user_exists = get_user_model().objects.filter(
        email=payload['email']
    ).exists()

    assert not user_exists
    err_msg = 'Ensure this field has at least 8 characters.'
    assert resp.json()['password'] == [err_msg]


def test_get_request_fails_at_create_endpoint(client):
    """Make sure that the GET method is not allowed at the create endpoint"""
    resp = client.get(CREATE_USER_URL)
    assert resp.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
