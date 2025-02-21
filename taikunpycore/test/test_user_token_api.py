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

from taikunpycore.api.user_token_api import UserTokenApi


class TestUserTokenApi(unittest.TestCase):
    """UserTokenApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserTokenApi()

    def tearDown(self) -> None:
        pass

    def test_usertoken_available_endpoints(self) -> None:
        """Test case for usertoken_available_endpoints

        Get available endpoint list
        """
        pass

    def test_usertoken_bind_unbind(self) -> None:
        """Test case for usertoken_bind_unbind

        Bind and unbind endpoints
        """
        pass

    def test_usertoken_create(self) -> None:
        """Test case for usertoken_create

        Create a new user token
        """
        pass

    def test_usertoken_delete(self) -> None:
        """Test case for usertoken_delete

        Delete user token
        """
        pass

    def test_usertoken_list(self) -> None:
        """Test case for usertoken_list

        Get user token list
        """
        pass


if __name__ == '__main__':
    unittest.main()
