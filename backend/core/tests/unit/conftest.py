# SPDX-License-Identifier: AGPL-3.0-or-later
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.fixture
def api_client() -> APIClient:
    return APIClient()

@pytest.fixture
def authenticated_client(api_client) -> APIClient:
    """
    Provides an authenticated API client for testing.
    
    Creates a test user and forces authentication for all requests made with this client.
    This eliminates the need to manually handle authentication in most test cases.
    """
    User = get_user_model() 
    user = User.objects.create_user(
        username="testuser",
        password="testpass123",
        email="testuser@example.com"
    )
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture(autouse=True)
def turn_off_throttling(settings, request: pytest.FixtureRequest):
    """
    Automatically disables API throttling for all tests unless the test is marked with 'enable_throttling'.

    This fixture modifies the Django REST Framework settings to set throttle rates for both anonymous and authenticated users to None.
    This effectively turns off request throttling during test execution.
    If the test is explicitly marked with 'enable_throttling', this fixture does not alter the throttling settings.

    Parameters
    ----------
    settings : django.conf.settings
        The Django settings fixture, used to modify REST framework configuration.

    request : pytest.FixtureRequest)
        Provides information about the requesting test function, including markers.

    Notes
    -----
    To enable throttling for a specific test, mark it with @pytest.mark.enable_throttling.
    """
    if "enable_throttling" in request.keywords:
        # If the test has the disable_throttling marker, skip this fixture.
        return

    settings.REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
        "anon": None,
        "user": None,
    }
