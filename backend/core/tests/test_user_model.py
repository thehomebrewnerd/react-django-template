import pytest
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_create_user_with_email_successful():
    """
    Test that creating a new user with email as username is successful
    """
    email = 'test@example.com'
    password = 'testpass123'
    first_name = 'Firstname'
    last_name = 'Lastname'

    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    assert user.email == email
    assert user.check_password(password)
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.is_active
    assert not user.is_staff


@pytest.mark.django_db
def test_new_user_email_normalized():
    """
    Test that the email address is normalized for new users so that
    address is not case sensitive.
    """
    email = 'test@EXAMPLE.com'
    user = get_user_model().objects.create_user(
        email=email,
        password="password123"
    )

    assert user.email == email.lower()


@pytest.mark.django_db
def test_user_email_unique_is_enforced():
    """
    Test that the unique email address constraint is properly enforced
    """
    email = 'test@example.com'
    get_user_model().objects.create_user(
        email=email,
        password="password123"
    )
    with pytest.raises(IntegrityError) as e:
        get_user_model().objects.create_user(
            email=email,
            password="password123"
        )
    assert str(e.value) == 'UNIQUE constraint failed: core_user.email'


@pytest.mark.django_db
def test_new_user_with_no_email_raises_error():
    """
    Test that creating a user with invlid email raises and error.
    """
    email = None

    with pytest.raises(ValueError) as e:
        get_user_model().objects.create_user(
            email=email,
            password="password123"
        )
    assert str(e.value) == 'No value provided for user `email`.'


@pytest.mark.django_db
def test_create_new_superuser():
    """
    Test creating a new superuser.
    """

    user = get_user_model().objects.create_superuser(
        email="test@example.com",
        password="password123"
    )

    assert user.is_superuser
    assert user.is_staff
