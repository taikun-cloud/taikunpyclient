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

from taikunpycore.api.ntp_servers_api import NtpServersApi


class TestNtpServersApi(unittest.TestCase):
    """NtpServersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NtpServersApi()

    def tearDown(self) -> None:
        pass

    def test_ntpservers_create(self) -> None:
        """Test case for ntpservers_create

        Create access profile ntp server
        """
        pass

    def test_ntpservers_delete(self) -> None:
        """Test case for ntpservers_delete

        Delete access profile ntp server
        """
        pass

    def test_ntpservers_edit(self) -> None:
        """Test case for ntpservers_edit

        Edit access profile ntp server
        """
        pass

    def test_ntpservers_list(self) -> None:
        """Test case for ntpservers_list

        List ntp server by access profile id
        """
        pass


if __name__ == '__main__':
    unittest.main()
