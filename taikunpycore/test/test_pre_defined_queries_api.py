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

from taikunpycore.api.pre_defined_queries_api import PreDefinedQueriesApi


class TestPreDefinedQueriesApi(unittest.TestCase):
    """PreDefinedQueriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PreDefinedQueriesApi()

    def tearDown(self) -> None:
        pass

    def test_predefinedqueries_create(self) -> None:
        """Test case for predefinedqueries_create

        Create prometheus dashboard pre defined query
        """
        pass

    def test_predefinedqueries_delete(self) -> None:
        """Test case for predefinedqueries_delete

        Delete prometheus dashboard pre defined query
        """
        pass

    def test_predefinedqueries_list(self) -> None:
        """Test case for predefinedqueries_list

        Get list of pre defined organization prometheus dashboard elements
        """
        pass

    def test_predefinedqueries_prometheus_dashboard_common(self) -> None:
        """Test case for predefinedqueries_prometheus_dashboard_common

        et list of pre defined common prometheus dashboard elements
        """
        pass

    def test_predefinedqueries_update(self) -> None:
        """Test case for predefinedqueries_update

        Update prometheus dashboard pre defined query
        """
        pass


if __name__ == '__main__':
    unittest.main()
