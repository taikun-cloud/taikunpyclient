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

from taikunpycore.models.operation_credentials import OperationCredentials

class TestOperationCredentials(unittest.TestCase):
    """OperationCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OperationCredentials:
        """Test OperationCredentials
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperationCredentials`
        """
        model = OperationCredentials()
        if include_optional:
            return OperationCredentials(
                data = [
                    taikunpycore.models.operation_credentials_list_dto.OperationCredentialsListDto(
                        id = 56, 
                        name = '', 
                        prometheus_username = '', 
                        prometheus_url = '', 
                        organization_id = 56, 
                        organization_name = '', 
                        is_locked = True, 
                        rules = [
                            taikunpycore.models.simple_prometheus_entity.SimplePrometheusEntity(
                                prometheus_rule_id = 56, 
                                prometheus_rule_name = '', )
                            ], 
                        created_by = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        is_default = True, )
                    ],
                total_count = 56
            )
        else:
            return OperationCredentials(
                data = [
                    taikunpycore.models.operation_credentials_list_dto.OperationCredentialsListDto(
                        id = 56, 
                        name = '', 
                        prometheus_username = '', 
                        prometheus_url = '', 
                        organization_id = 56, 
                        organization_name = '', 
                        is_locked = True, 
                        rules = [
                            taikunpycore.models.simple_prometheus_entity.SimplePrometheusEntity(
                                prometheus_rule_id = 56, 
                                prometheus_rule_name = '', )
                            ], 
                        created_by = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        is_default = True, )
                    ],
                total_count = 56,
        )
        """

    def testOperationCredentials(self):
        """Test OperationCredentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
