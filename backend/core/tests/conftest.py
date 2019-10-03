import pytest
from django.contrib.auth import get_user_model
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def admin_user():
    return get_user_model().objects.create_superuser(
        email="admin@test.com",
        password="password123"
    )


@pytest.fixture
def regular_user():
    return get_user_model().objects.create_user(
        email="user@test.com",
        password="password123",
        first_name="Johnny",
        last_name="User"
    )
