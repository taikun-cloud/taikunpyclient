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

from taikunpycore.api.standalone_api import StandaloneApi


class TestStandaloneApi(unittest.TestCase):
    """StandaloneApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StandaloneApi()

    def tearDown(self) -> None:
        pass

    def test_standalone_create(self) -> None:
        """Test case for standalone_create

        Create a new vm in the given project.
        """
        pass

    def test_standalone_details(self) -> None:
        """Test case for standalone_details

        Retrieve a list of standalone vm with detailed info
        """
        pass

    def test_standalone_ip_management(self) -> None:
        """Test case for standalone_ip_management

        Enable/Disable stand alone public ip
        """
        pass

    def test_standalone_list(self) -> None:
        """Test case for standalone_list

        Retrieve all vms
        """
        pass

    def test_standalone_reset(self) -> None:
        """Test case for standalone_reset

        Reset vm status
        """
        pass

    def test_standalone_update_flavor(self) -> None:
        """Test case for standalone_update_flavor

        Update standalone vm flavor
        """
        pass


if __name__ == '__main__':
    unittest.main()
