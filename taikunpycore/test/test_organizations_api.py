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

from taikunpycore.api.organizations_api import OrganizationsApi


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_organizations_accept_offer(self) -> None:
        """Test case for organizations_accept_offer

        Accept discount offer
        """
        pass

    def test_organizations_access_for_partner(self) -> None:
        """Test case for organizations_access_for_partner

        Give access to partner
        """
        pass

    def test_organizations_add_prometheusrules(self) -> None:
        """Test case for organizations_add_prometheusrules

        Add prometheus rule(s) to organization
        """
        pass

    def test_organizations_create(self) -> None:
        """Test case for organizations_create

        Add a new organization. Only available for admins.
        """
        pass

    def test_organizations_delete(self) -> None:
        """Test case for organizations_delete

        Delete the specified organization. Only available for admins.
        """
        pass

    def test_organizations_delete_prometheusrules(self) -> None:
        """Test case for organizations_delete_prometheusrules

        Delete prometheus rule(s) from organization
        """
        pass

    def test_organizations_detawils(self) -> None:
        """Test case for organizations_detawils

        Retrieve all data about current organization by Id
        """
        pass

    def test_organizations_export_csv(self) -> None:
        """Test case for organizations_export_csv

        Export Csv file
        """
        pass

    def test_organizations_leave(self) -> None:
        """Test case for organizations_leave

        Leave taikun
        """
        pass

    def test_organizations_list(self) -> None:
        """Test case for organizations_list

        Retrieve all organizations
        """
        pass

    def test_organizations_organization_list(self) -> None:
        """Test case for organizations_organization_list

        Retrieve organizations
        """
        pass

    def test_organizations_toggle(self) -> None:
        """Test case for organizations_toggle

        Toggle keycloak login option
        """
        pass

    def test_organizations_update(self) -> None:
        """Test case for organizations_update

        Update organization by Id
        """
        pass

    def test_organizations_update_payment(self) -> None:
        """Test case for organizations_update_payment

        Update organization payment Id
        """
        pass


if __name__ == '__main__':
    unittest.main()
