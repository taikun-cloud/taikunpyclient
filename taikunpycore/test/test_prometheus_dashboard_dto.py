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

from taikunpycore.models.prometheus_dashboard_dto import PrometheusDashboardDto

class TestPrometheusDashboardDto(unittest.TestCase):
    """PrometheusDashboardDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrometheusDashboardDto:
        """Test PrometheusDashboardDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrometheusDashboardDto`
        """
        model = PrometheusDashboardDto()
        if include_optional:
            return PrometheusDashboardDto(
                id = 56,
                name = '',
                expression_decoded = '',
                expression_encoded = '',
                description = '',
                is_readonly = True
            )
        else:
            return PrometheusDashboardDto(
                id = 56,
                name = '',
                expression_decoded = '',
                expression_encoded = '',
                description = '',
                is_readonly = True,
        )
        """

    def testPrometheusDashboardDto(self):
        """Test PrometheusDashboardDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
