"""Test views."""
from django.urls import reverse_lazy


def test_home_view(client):
    """Test home view."""
    url = reverse_lazy("core:home")
    response = client.get(url)
    assert response.status_code == 200
