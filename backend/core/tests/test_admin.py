import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_users_listed(client, admin_user, regular_user):
    """Test that users are listed on the admin user page"""
    client.force_login(admin_user)
    url = reverse('admin:core_user_changelist')
    resp = client.get(url)

    assert resp.status_code == 200
    assert regular_user.first_name in str(resp.content)
    assert regular_user.last_name in str(resp.content)
    assert regular_user.email in str(resp.content)


@pytest.mark.django_db
def test_user_change_page(client, admin_user, regular_user):
    """Test that the user edit page works"""
    client.force_login(admin_user)
    url = reverse('admin:core_user_change', args=[regular_user.id])
    resp = client.get(url)

    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_create_page(client, admin_user):
    """Test that the admin create user page works"""
    client.force_login(admin_user)
    url = reverse('admin:core_user_add')
    resp = client.get(url)

    assert resp.status_code == 200
