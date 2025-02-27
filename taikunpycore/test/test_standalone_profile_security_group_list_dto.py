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

from taikunpycore.models.standalone_profile_security_group_list_dto import StandaloneProfileSecurityGroupListDto

class TestStandaloneProfileSecurityGroupListDto(unittest.TestCase):
    """StandaloneProfileSecurityGroupListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandaloneProfileSecurityGroupListDto:
        """Test StandaloneProfileSecurityGroupListDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandaloneProfileSecurityGroupListDto`
        """
        model = StandaloneProfileSecurityGroupListDto()
        if include_optional:
            return StandaloneProfileSecurityGroupListDto(
                id = 56,
                name = '',
                protocol = '',
                port_min_range = 56,
                port_max_range = 56,
                remote_ip_prefix = ''
            )
        else:
            return StandaloneProfileSecurityGroupListDto(
                id = 56,
                name = '',
                protocol = '',
                port_min_range = 56,
                port_max_range = 56,
                remote_ip_prefix = '',
        )
        """

    def testStandaloneProfileSecurityGroupListDto(self):
        """Test StandaloneProfileSecurityGroupListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
