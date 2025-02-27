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

from taikunpycore.models.create_subscription_command import CreateSubscriptionCommand

class TestCreateSubscriptionCommand(unittest.TestCase):
    """CreateSubscriptionCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSubscriptionCommand:
        """Test CreateSubscriptionCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubscriptionCommand`
        """
        model = CreateSubscriptionCommand()
        if include_optional:
            return CreateSubscriptionCommand(
                name = '',
                project_limit = 56,
                server_limit = 56,
                user_limit = 56,
                cloud_credential_limit = 56,
                trial_days = 56,
                monthly_price = 1.337,
                tcu_price = 1.337,
                yearly_price = 1.337
            )
        else:
            return CreateSubscriptionCommand(
        )
        """

    def testCreateSubscriptionCommand(self):
        """Test CreateSubscriptionCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
