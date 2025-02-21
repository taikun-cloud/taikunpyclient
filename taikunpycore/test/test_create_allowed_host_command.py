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

from taikunpycore.models.create_allowed_host_command import CreateAllowedHostCommand

class TestCreateAllowedHostCommand(unittest.TestCase):
    """CreateAllowedHostCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAllowedHostCommand:
        """Test CreateAllowedHostCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAllowedHostCommand`
        """
        model = CreateAllowedHostCommand()
        if include_optional:
            return CreateAllowedHostCommand(
                access_profile_id = 56,
                description = '',
                ip_address = '',
                mask_bits = 56
            )
        else:
            return CreateAllowedHostCommand(
        )
        """

    def testCreateAllowedHostCommand(self):
        """Test CreateAllowedHostCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
