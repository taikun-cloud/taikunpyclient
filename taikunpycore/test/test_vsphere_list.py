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

from taikunpycore.models.vsphere_list import VsphereList

class TestVsphereList(unittest.TestCase):
    """VsphereList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VsphereList:
        """Test VsphereList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VsphereList`
        """
        model = VsphereList()
        if include_optional:
            return VsphereList(
                data = [
                    taikunpycore.models.vsphere_list_dto.VsphereListDto(
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
                        drs_enabled = True, 
                        resource_pool = '', 
                        organization_id = 56, 
                        organization_name = '', 
                        continent_name = '', 
                        hypervisors = [
                            taikunpycore.models.common_string_based_dropdown_dto.CommonStringBasedDropdownDto(
                                id = '', 
                                name = '', )
                            ], 
                        username = '', 
                        url = '', 
                        datacenter_id = '', 
                        datacenter_name = '', 
                        datastore = '', 
                        vm_template_name = '', 
                        vsphere_networks = [
                            taikunpycore.models.vsphere_network_list_dto.VsphereNetworkListDto(
                                name = '', 
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
            return VsphereList(
                data = [
                    taikunpycore.models.vsphere_list_dto.VsphereListDto(
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
                        drs_enabled = True, 
                        resource_pool = '', 
                        organization_id = 56, 
                        organization_name = '', 
                        continent_name = '', 
                        hypervisors = [
                            taikunpycore.models.common_string_based_dropdown_dto.CommonStringBasedDropdownDto(
                                id = '', 
                                name = '', )
                            ], 
                        username = '', 
                        url = '', 
                        datacenter_id = '', 
                        datacenter_name = '', 
                        datastore = '', 
                        vm_template_name = '', 
                        vsphere_networks = [
                            taikunpycore.models.vsphere_network_list_dto.VsphereNetworkListDto(
                                name = '', 
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

    def testVsphereList(self):
        """Test VsphereList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
