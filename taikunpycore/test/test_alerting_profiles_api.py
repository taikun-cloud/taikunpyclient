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

from taikunpycore.api.alerting_profiles_api import AlertingProfilesApi


class TestAlertingProfilesApi(unittest.TestCase):
    """AlertingProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AlertingProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_alertingprofiles_assign_email(self) -> None:
        """Test case for alertingprofiles_assign_email

        Assign Alerting emails
        """
        pass

    def test_alertingprofiles_assign_webhooks(self) -> None:
        """Test case for alertingprofiles_assign_webhooks

        Assign Alerting webhooks
        """
        pass

    def test_alertingprofiles_attach(self) -> None:
        """Test case for alertingprofiles_attach

        Attach alerting profile to project
        """
        pass

    def test_alertingprofiles_create(self) -> None:
        """Test case for alertingprofiles_create

        Add Alerting profile
        """
        pass

    def test_alertingprofiles_delete(self) -> None:
        """Test case for alertingprofiles_delete

        Remove Alerting profiles by Id
        """
        pass

    def test_alertingprofiles_detach(self) -> None:
        """Test case for alertingprofiles_detach

        Detach alerting profile from project
        """
        pass

    def test_alertingprofiles_dropdown(self) -> None:
        """Test case for alertingprofiles_dropdown

        Retrieve all Alerting profiles for organization
        """
        pass

    def test_alertingprofiles_edit(self) -> None:
        """Test case for alertingprofiles_edit

        Update Alerting profile
        """
        pass

    def test_alertingprofiles_list(self) -> None:
        """Test case for alertingprofiles_list

        Retrieve all Alerting profiles
        """
        pass

    def test_alertingprofiles_lock_manager(self) -> None:
        """Test case for alertingprofiles_lock_manager

        Lock/Unlock Alerting profiles
        """
        pass

    def test_alertingprofiles_verify(self) -> None:
        """Test case for alertingprofiles_verify

        Verify webhook endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()
