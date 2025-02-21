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

from taikunpycore.models.allowed_host_create_dto import AllowedHostCreateDto

class TestAllowedHostCreateDto(unittest.TestCase):
    """AllowedHostCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllowedHostCreateDto:
        """Test AllowedHostCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllowedHostCreateDto`
        """
        model = AllowedHostCreateDto()
        if include_optional:
            return AllowedHostCreateDto(
                description = '',
                ip_address = '',
                mask_bits = 56
            )
        else:
            return AllowedHostCreateDto(
        )
        """

    def testAllowedHostCreateDto(self):
        """Test AllowedHostCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
