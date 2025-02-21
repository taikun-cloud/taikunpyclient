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

from taikunpycore.models.proxmox_list import ProxmoxList

class TestProxmoxList(unittest.TestCase):
    """ProxmoxList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProxmoxList:
        """Test ProxmoxList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProxmoxList`
        """
        model = ProxmoxList()
        if include_optional:
            return ProxmoxList(
                data = [
                    taikunpycore.models.proxmox_list_dto.ProxmoxListDto(
                        id = 56, 
                        project_count = 56, 
                        is_locked = True, 
                        name = '', 
                        projects = [
                            taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                                id = 56, 
                                name = '', )
                            ], 
                        created_by = '', 
                        created_at = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        is_default = True, 
                        organization_id = 56, 
                        organization_name = '', 
                        continent_name = '', 
                        hypervisors = [
                            taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                                id = 56, 
                                name = '', )
                            ], 
                        token_id = '', 
                        url = '', 
                        storage = '', 
                        vm_template_name = '', 
                        proxmox_networks = [
                            taikunpycore.models.proxmox_network_list_dto.ProxmoxNetworkListDto(
                                bridge = '', 
                                gateway = '', 
                                ip_address = '', 
                                net_mask = 56, 
                                begin_allocation_range = '', 
                                end_allocation_range = '', 
                                is_private = True, 
                                is_virtual_lb_network = True, )
                            ], 
                        skip_tls_flag = True, )
                    ],
                total_count = 56
            )
        else:
            return ProxmoxList(
                data = [
                    taikunpycore.models.proxmox_list_dto.ProxmoxListDto(
                        id = 56, 
                        project_count = 56, 
                        is_locked = True, 
                        name = '', 
                        projects = [
                            taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                                id = 56, 
                                name = '', )
                            ], 
                        created_by = '', 
                        created_at = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        is_default = True, 
                        organization_id = 56, 
                        organization_name = '', 
                        continent_name = '', 
                        hypervisors = [
                            taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                                id = 56, 
                                name = '', )
                            ], 
                        token_id = '', 
                        url = '', 
                        storage = '', 
                        vm_template_name = '', 
                        proxmox_networks = [
                            taikunpycore.models.proxmox_network_list_dto.ProxmoxNetworkListDto(
                                bridge = '', 
                                gateway = '', 
                                ip_address = '', 
                                net_mask = 56, 
                                begin_allocation_range = '', 
                                end_allocation_range = '', 
                                is_private = True, 
                                is_virtual_lb_network = True, )
                            ], 
                        skip_tls_flag = True, )
                    ],
                total_count = 56,
        )
        """

    def testProxmoxList(self):
        """Test ProxmoxList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
