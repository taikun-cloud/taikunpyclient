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

from taikunpycore.models.create_vsphere_command import CreateVsphereCommand

class TestCreateVsphereCommand(unittest.TestCase):
    """CreateVsphereCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateVsphereCommand:
        """Test CreateVsphereCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateVsphereCommand`
        """
        model = CreateVsphereCommand()
        if include_optional:
            return CreateVsphereCommand(
                name = '',
                username = '',
                url = '',
                password = '',
                datacenter_id = '',
                datacenter_name = '',
                datastore_name = '',
                resource_pool_name = '',
                drs_enabled = True,
                vm_template_name = '',
                continent = '',
                organization_id = 56,
                hypervisors = [
                    ''
                    ],
                public_network = taikunpycore.models.create_vsphere_network_dto.CreateVsphereNetworkDto(
                    name = '', 
                    gateway = '', 
                    ip_address = '', 
                    net_mask = 56, 
                    begin_allocation_range = '', 
                    end_allocation_range = '', ),
                private_network = taikunpycore.models.create_vsphere_network_dto.CreateVsphereNetworkDto(
                    name = '', 
                    gateway = '', 
                    ip_address = '', 
                    net_mask = 56, 
                    begin_allocation_range = '', 
                    end_allocation_range = '', ),
                skip_tls_flag = True
            )
        else:
            return CreateVsphereCommand(
        )
        """

    def testCreateVsphereCommand(self):
        """Test CreateVsphereCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
