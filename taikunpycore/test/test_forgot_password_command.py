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

from taikunpycore.models.forgot_password_command import ForgotPasswordCommand

class TestForgotPasswordCommand(unittest.TestCase):
    """ForgotPasswordCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ForgotPasswordCommand:
        """Test ForgotPasswordCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ForgotPasswordCommand`
        """
        model = ForgotPasswordCommand()
        if include_optional:
            return ForgotPasswordCommand(
                email = ''
            )
        else:
            return ForgotPasswordCommand(
        )
        """

    def testForgotPasswordCommand(self):
        """Test ForgotPasswordCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
