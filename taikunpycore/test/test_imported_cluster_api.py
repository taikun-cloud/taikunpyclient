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

from taikunpycore.api.imported_cluster_api import ImportedClusterApi


class TestImportedClusterApi(unittest.TestCase):
    """ImportedClusterApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ImportedClusterApi()

    def tearDown(self) -> None:
        pass

    def test_imported_cluster_as_cloud_credential(self) -> None:
        """Test case for imported_cluster_as_cloud_credential

        Imported cluster as cloud credential
        """
        pass

    def test_imported_cluster_as_fully_managed(self) -> None:
        """Test case for imported_cluster_as_fully_managed

        Imported cluster as fully managed
        """
        pass

    def test_imported_cluster_as_read_only(self) -> None:
        """Test case for imported_cluster_as_read_only

        Imported cluster as read only
        """
        pass

    def test_imported_cluster_delete(self) -> None:
        """Test case for imported_cluster_delete

        Delete imported cluster
        """
        pass

    def test_imported_cluster_details(self) -> None:
        """Test case for imported_cluster_details

        Retrieve imported-cluster by given id
        """
        pass

    def test_imported_cluster_disable_ai(self) -> None:
        """Test case for imported_cluster_disable_ai

        Disable ai for imported cluster
        """
        pass

    def test_imported_cluster_disable_backup(self) -> None:
        """Test case for imported_cluster_disable_backup

        Disable backup for imported cluster
        """
        pass

    def test_imported_cluster_disable_monitoring(self) -> None:
        """Test case for imported_cluster_disable_monitoring

        Disable monitoring for imported cluster
        """
        pass

    def test_imported_cluster_disable_opa(self) -> None:
        """Test case for imported_cluster_disable_opa

        Disable opa for imported cluster
        """
        pass

    def test_imported_cluster_enable_ai(self) -> None:
        """Test case for imported_cluster_enable_ai

        Enable ai for imported cluster
        """
        pass

    def test_imported_cluster_enable_backup(self) -> None:
        """Test case for imported_cluster_enable_backup

        Enable backup for imported cluster
        """
        pass

    def test_imported_cluster_enable_monitoring(self) -> None:
        """Test case for imported_cluster_enable_monitoring

        Enable monitoring for imported cluster
        """
        pass

    def test_imported_cluster_enable_opa(self) -> None:
        """Test case for imported_cluster_enable_opa

        Enable opa for imported cluster
        """
        pass


if __name__ == '__main__':
    unittest.main()
