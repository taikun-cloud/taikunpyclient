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

from taikunpycore.api.access_profiles_api import AccessProfilesApi


class TestAccessProfilesApi(unittest.TestCase):
    """AccessProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccessProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_accessprofiles_create(self) -> None:
        """Test case for accessprofiles_create

        Create access profile
        """
        pass

    def test_accessprofiles_delete(self) -> None:
        """Test case for accessprofiles_delete

        Delete access profile by Id
        """
        pass

    def test_accessprofiles_dropdown(self) -> None:
        """Test case for accessprofiles_dropdown

        Retrieve access profiles by organization Id
        """
        pass

    def test_accessprofiles_list(self) -> None:
        """Test case for accessprofiles_list

        Retrieve all access profiles
        """
        pass

    def test_accessprofiles_lock_manager(self) -> None:
        """Test case for accessprofiles_lock_manager

        Lock/unlock access profiles
        """
        pass

    def test_accessprofiles_update(self) -> None:
        """Test case for accessprofiles_update

        Update access profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
