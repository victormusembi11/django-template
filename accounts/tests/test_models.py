"""Accounts app models unit tests."""
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_user_create(user):
    """Test user creation."""
    assert user.pk == 1, "Should save an instance of the User model"


@pytest.mark.django_db
def test_user_str(user):
    """Test user string representation."""
    assert str(user) == user.email, "Should return the user email"


@pytest.mark.django_db
def test_missing_email(user_data):
    """Test missing email raises error."""
    user_data["email"] = None
    with pytest.raises(ValueError):
        user = User.objects.create_user(**user_data)
        user.full_clean()


@pytest.mark.django_db
def test_create_superuser(superuser):
    """Test creating a superuser."""
    assert superuser.email == "test@example.com"
    assert superuser.check_password("testpassword")
    assert superuser.is_staff
    assert superuser.is_superuser


@pytest.mark.django_db
def test_create_superuser_non_staff(user_data):
    """Test creating a superuser w/ is_staff=False raises an error."""
    user_data["is_staff"] = False
    with pytest.raises(ValueError):
        User.objects.create_superuser(**user_data)


@pytest.mark.django_db
def test_create_superuser_non_superuser(user_data):
    """Test creating a superuser with is_superuser=False raises an error."""
    user_data["is_superuser"] = False
    with pytest.raises(ValueError):
        User.objects.create_superuser(**user_data)
