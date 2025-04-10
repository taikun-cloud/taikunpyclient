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

from taikunpycore.api.proxmox_cloud_credential_api import ProxmoxCloudCredentialApi


class TestProxmoxCloudCredentialApi(unittest.TestCase):
    """ProxmoxCloudCredentialApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProxmoxCloudCredentialApi()

    def tearDown(self) -> None:
        pass

    def test_proxmox_bridge_list(self) -> None:
        """Test case for proxmox_bridge_list

        Fetch proxmox bridge list
        """
        pass

    def test_proxmox_create(self) -> None:
        """Test case for proxmox_create

        Add Proxmox credentials
        """
        pass

    def test_proxmox_hypervisor_list(self) -> None:
        """Test case for proxmox_hypervisor_list

        Fetch proxmox hypervisor list
        """
        pass

    def test_proxmox_list(self) -> None:
        """Test case for proxmox_list

        Retrieve list of proxmox cloud credentials
        """
        pass

    def test_proxmox_storage_list(self) -> None:
        """Test case for proxmox_storage_list

        Fetch proxmox storage list
        """
        pass

    def test_proxmox_update(self) -> None:
        """Test case for proxmox_update

        Update proxmox credentials
        """
        pass

    def test_proxmox_update_hypervisors(self) -> None:
        """Test case for proxmox_update_hypervisors

        Update proxmox credentials
        """
        pass

    def test_proxmox_update_ip_addresses(self) -> None:
        """Test case for proxmox_update_ip_addresses

        Update proxmox network used ip addresses
        """
        pass

    def test_proxmox_vm_template_list(self) -> None:
        """Test case for proxmox_vm_template_list

        Fetch proxmox vm template list
        """
        pass


if __name__ == '__main__':
    unittest.main()
