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

from taikunpycore.api.notifications_api import NotificationsApi


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationsApi()

    def tearDown(self) -> None:
        pass

    def test_notifications_create(self) -> None:
        """Test case for notifications_create

        Create notification
        """
        pass

    def test_notifications_export_csv(self) -> None:
        """Test case for notifications_export_csv

        Export Csv
        """
        pass

    def test_notifications_list(self) -> None:
        """Test case for notifications_list

        Retrieve all notifications
        """
        pass

    def test_notifications_notify_owner(self) -> None:
        """Test case for notifications_notify_owner

        Notify owner
        """
        pass

    def test_notifications_operation_messages(self) -> None:
        """Test case for notifications_operation_messages

        Get project operations
        """
        pass


if __name__ == '__main__':
    unittest.main()
