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

from taikunpycore.api.invoices_api import InvoicesApi


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvoicesApi()

    def tearDown(self) -> None:
        pass

    def test_invoices_create(self) -> None:
        """Test case for invoices_create

        Create invoice
        """
        pass

    def test_invoices_download(self) -> None:
        """Test case for invoices_download

        Download invoice
        """
        pass

    def test_invoices_list(self) -> None:
        """Test case for invoices_list

        Invoices list
        """
        pass

    def test_invoices_update(self) -> None:
        """Test case for invoices_update

        Update invoice
        """
        pass


if __name__ == '__main__':
    unittest.main()
