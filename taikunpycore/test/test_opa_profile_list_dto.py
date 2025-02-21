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

from taikunpycore.models.opa_profile_list_dto import OpaProfileListDto

class TestOpaProfileListDto(unittest.TestCase):
    """OpaProfileListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpaProfileListDto:
        """Test OpaProfileListDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpaProfileListDto`
        """
        model = OpaProfileListDto()
        if include_optional:
            return OpaProfileListDto(
                id = 56,
                name = '',
                forbid_node_port = True,
                forbid_http_ingress = True,
                require_probe = True,
                unique_ingresses = True,
                unique_service_selector = True,
                force_pod_resource = True,
                is_node_name_forbidden_in_vc = True,
                is_master_taint_enforced = True,
                whitelist_master_taint_namespaces = [
                    ''
                    ],
                allowed_repo = [
                    ''
                    ],
                forbid_specific_tags = [
                    ''
                    ],
                ingress_whitelist = [
                    ''
                    ],
                is_locked = True,
                revision = 56,
                organization_id = 56,
                organization_name = '',
                created_at = '',
                is_default = True,
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ]
            )
        else:
            return OpaProfileListDto(
                id = 56,
                name = '',
                forbid_node_port = True,
                forbid_http_ingress = True,
                require_probe = True,
                unique_ingresses = True,
                unique_service_selector = True,
                force_pod_resource = True,
                is_node_name_forbidden_in_vc = True,
                is_master_taint_enforced = True,
                whitelist_master_taint_namespaces = [
                    ''
                    ],
                allowed_repo = [
                    ''
                    ],
                forbid_specific_tags = [
                    ''
                    ],
                ingress_whitelist = [
                    ''
                    ],
                is_locked = True,
                revision = 56,
                organization_id = 56,
                organization_name = '',
                created_at = '',
                is_default = True,
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
        )
        """

    def testOpaProfileListDto(self):
        """Test OpaProfileListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
