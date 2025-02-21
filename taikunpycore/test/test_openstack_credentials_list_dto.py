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

from taikunpycore.models.openstack_credentials_list_dto import OpenstackCredentialsListDto

class TestOpenstackCredentialsListDto(unittest.TestCase):
    """OpenstackCredentialsListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenstackCredentialsListDto:
        """Test OpenstackCredentialsListDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenstackCredentialsListDto`
        """
        model = OpenstackCredentialsListDto()
        if include_optional:
            return OpenstackCredentialsListDto(
                id = 56,
                project_count = 56,
                is_locked = True,
                name = '',
                user = '',
                url = '',
                project = '',
                domain = '',
                region = '',
                public_network = '',
                import_network = True,
                tenant_id = '',
                availability_zone = '',
                volume_type = '',
                internal_subnet_id = '',
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
                created_by = '',
                last_modified = '',
                last_modified_by = '',
                is_default = True,
                organization_id = 56,
                organization_name = '',
                created_at = '',
                continent_name = '',
                is_admin = True,
                is_infra = True,
                application_cred_enabled = True,
                skip_tls_flag = True
            )
        else:
            return OpenstackCredentialsListDto(
                id = 56,
                project_count = 56,
                is_locked = True,
                name = '',
                user = '',
                url = '',
                project = '',
                domain = '',
                region = '',
                public_network = '',
                import_network = True,
                tenant_id = '',
                availability_zone = '',
                volume_type = '',
                internal_subnet_id = '',
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
                created_by = '',
                last_modified = '',
                last_modified_by = '',
                is_default = True,
                organization_id = 56,
                organization_name = '',
                created_at = '',
                continent_name = '',
                is_admin = True,
                is_infra = True,
                application_cred_enabled = True,
                skip_tls_flag = True,
        )
        """

    def testOpenstackCredentialsListDto(self):
        """Test OpenstackCredentialsListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
