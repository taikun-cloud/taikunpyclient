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

from taikunpycore.models.openstack_quota_list import OpenstackQuotaList

class TestOpenstackQuotaList(unittest.TestCase):
    """OpenstackQuotaList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenstackQuotaList:
        """Test OpenstackQuotaList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenstackQuotaList`
        """
        model = OpenstackQuotaList()
        if include_optional:
            return OpenstackQuotaList(
                compute = taikunpycore.models.openstack_compute_quota_dto.OpenstackComputeQuotaDto(
                    max_total_ram_size = 56, 
                    max_server_groups = 56, 
                    max_total_instances = 56, 
                    max_total_cores = 56, 
                    used_ram_size = 56, 
                    used_cpu_size = 56, 
                    used_instance_size = 56, 
                    used_server_groups = 56, ),
                volume = taikunpycore.models.openstack_volume_quota_dto.OpenstackVolumeQuotaDto(
                    max_total_volume_size = 56, 
                    used_volume_size = 56, 
                    max_count_volume_size = 56, 
                    count_volume_size = 56, ),
                network = taikunpycore.models.openstack_network_dto.OpenstackNetworkDto(
                    network_limit = 56, 
                    subnet_limit = 56, 
                    floating_ip_limit = 56, 
                    router_limit = 56, 
                    security_group_limit = 56, 
                    security_group_rule_limit = 56, 
                    port_limit = 56, 
                    network_used = 56, 
                    subnet_used = 56, 
                    floating_ip_used = 56, 
                    router_used = 56, 
                    security_group_used = 56, 
                    port_used = 56, 
                    security_group_rule_used = 56, ),
                is_infra = True
            )
        else:
            return OpenstackQuotaList(
        )
        """

    def testOpenstackQuotaList(self):
        """Test OpenstackQuotaList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
