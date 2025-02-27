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

from taikunpycore.models.cloud_credentials_for_organization_entity import CloudCredentialsForOrganizationEntity

class TestCloudCredentialsForOrganizationEntity(unittest.TestCase):
    """CloudCredentialsForOrganizationEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudCredentialsForOrganizationEntity:
        """Test CloudCredentialsForOrganizationEntity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudCredentialsForOrganizationEntity`
        """
        model = CloudCredentialsForOrganizationEntity()
        if include_optional:
            return CloudCredentialsForOrganizationEntity(
                id = 56,
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
                full_name = '',
                cloud_type = 'NONE',
                is_default = True
            )
        else:
            return CloudCredentialsForOrganizationEntity(
                id = 56,
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
                full_name = '',
                cloud_type = 'NONE',
                is_default = True,
        )
        """

    def testCloudCredentialsForOrganizationEntity(self):
        """Test CloudCredentialsForOrganizationEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
