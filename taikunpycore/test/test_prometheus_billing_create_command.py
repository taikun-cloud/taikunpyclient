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

from taikunpycore.models.prometheus_billing_create_command import PrometheusBillingCreateCommand

class TestPrometheusBillingCreateCommand(unittest.TestCase):
    """PrometheusBillingCreateCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrometheusBillingCreateCommand:
        """Test PrometheusBillingCreateCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrometheusBillingCreateCommand`
        """
        model = PrometheusBillingCreateCommand()
        if include_optional:
            return PrometheusBillingCreateCommand(
                organization_id = 56,
                prometheus_rule_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                price = 1.337
            )
        else:
            return PrometheusBillingCreateCommand(
        )
        """

    def testPrometheusBillingCreateCommand(self):
        """Test PrometheusBillingCreateCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
