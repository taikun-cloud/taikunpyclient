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

from taikunpycore.models.summary import Summary

class TestSummary(unittest.TestCase):
    """Summary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Summary:
        """Test Summary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Summary`
        """
        model = Summary()
        if include_optional:
            return Summary(
                total_detected_resources = 56,
                total_supported_resources = 56,
                total_unsupported_resources = 56,
                total_usage_based_resources = 56,
                total_no_price_resources = 56,
                unsupported_resource_counts = {
                    'key' : 56
                    },
                no_price_resource_counts = {
                    'key' : 56
                    }
            )
        else:
            return Summary(
        )
        """

    def testSummary(self):
        """Test Summary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
