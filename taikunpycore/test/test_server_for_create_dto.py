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

from taikunpycore.models.server_for_create_dto import ServerForCreateDto

class TestServerForCreateDto(unittest.TestCase):
    """ServerForCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerForCreateDto:
        """Test ServerForCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerForCreateDto`
        """
        model = ServerForCreateDto()
        if include_optional:
            return ServerForCreateDto(
                name = '',
                role = 'Bastion',
                project_id = 56,
                disk_size = 1.337,
                flavor = '',
                count = 56,
                spot_price = 1.337,
                spot_instance = True,
                wasm_enabled = True,
                autoscaling_group = '',
                availability_zone = '',
                proxmox_extra_disk_size = 56,
                proxmox_role = 'NONE',
                hypervisor = '',
                kubernetes_node_labels = [
                    taikunpycore.models.kubernetes_node_labels_dto.KubernetesNodeLabelsDto(
                        key = '', 
                        value = '', )
                    ],
                replica_count = 56
            )
        else:
            return ServerForCreateDto(
        )
        """

    def testServerForCreateDto(self):
        """Test ServerForCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
