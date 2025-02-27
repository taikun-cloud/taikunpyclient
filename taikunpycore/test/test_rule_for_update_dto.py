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

from taikunpycore.models.rule_for_update_dto import RuleForUpdateDto

class TestRuleForUpdateDto(unittest.TestCase):
    """RuleForUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleForUpdateDto:
        """Test RuleForUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleForUpdateDto`
        """
        model = RuleForUpdateDto()
        if include_optional:
            return RuleForUpdateDto(
                name = '',
                metric_name = '',
                type = 'Count',
                price = 1.337,
                labels = [
                    taikunpycore.models.prometheus_label_list_dto.PrometheusLabelListDto(
                        label = '', 
                        value = '', )
                    ],
                operation_credential_id = 56
            )
        else:
            return RuleForUpdateDto(
        )
        """

    def testRuleForUpdateDto(self):
        """Test RuleForUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
