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

from taikunpycore.models.update_user_command import UpdateUserCommand

class TestUpdateUserCommand(unittest.TestCase):
    """UpdateUserCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserCommand:
        """Test UpdateUserCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserCommand`
        """
        model = UpdateUserCommand()
        if include_optional:
            return UpdateUserCommand(
                id = '',
                display_name = '',
                username = '',
                email = '',
                role = 'Admin',
                force_to_reset_password = True,
                disable = True,
                is_approved_by_partner = True
            )
        else:
            return UpdateUserCommand(
        )
        """

    def testUpdateUserCommand(self):
        """Test UpdateUserCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
