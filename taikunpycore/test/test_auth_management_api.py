# coding: utf-8

"""
    Taikun - WebApi

    This Api will be responsible for overall data distribution and authorization.

    The version of the OpenAPI document: v1
    Contact: noreply@taikun.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from taikunpycore.api.auth_management_api import AuthManagementApi


class TestAuthManagementApi(unittest.TestCase):
    """AuthManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthManagementApi()

    def tearDown(self) -> None:
        pass

    def test_auth_forgot_password(self) -> None:
        """Test case for auth_forgot_password

        Generate reset password token if you forgot password
        """
        pass

    def test_auth_google(self) -> None:
        """Test case for auth_google

        Consent to Google
        """
        pass

    def test_auth_login(self) -> None:
        """Test case for auth_login

        Login to API
        """
        pass

    def test_auth_refresh(self) -> None:
        """Test case for auth_refresh

        Refresh bearer token that generated automatically by API
        """
        pass

    def test_auth_reset_password(self) -> None:
        """Test case for auth_reset_password

        Reset password
        """
        pass

    def test_auth_trial(self) -> None:
        """Test case for auth_trial

        New registration
        """
        pass

    def test_auth_verify2fa(self) -> None:
        """Test case for auth_verify2fa

        Verify 2FA
        """
        pass


if __name__ == '__main__':
    unittest.main()
