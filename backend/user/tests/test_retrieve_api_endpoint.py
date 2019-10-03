import pytest
from django.urls import reverse
from rest_framework import status

RETRIEVE_USER_URL = reverse('user:retrieve', kwargs={'pk': 1})


@pytest.mark.django_db
def test_public_retrieve_existing_user(client, db_user):
    """Test retrieving an existing user is successful"""
    resp = client.get(RETRIEVE_USER_URL)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['first_name'] == db_user.first_name
    assert resp.json()['last_name'] == db_user.last_name
    assert resp.json()['email'] == db_user.email
    assert resp.json().get('password') is None
