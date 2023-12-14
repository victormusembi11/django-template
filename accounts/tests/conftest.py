"""Test fixtures for accounts app."""
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user_data():
    """Return user data for testing."""
    return {
        "email": "test@example.com",
        "password": "testpassword",
    }


@pytest.fixture
def user(user_data):
    """Return a user."""
    return User.objects.create_user(**user_data)


@pytest.fixture
def superuser(user_data):
    """Return a superuser."""
    return User.objects.create_superuser(**user_data)
