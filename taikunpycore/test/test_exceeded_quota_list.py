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

from taikunpycore.models.exceeded_quota_list import ExceededQuotaList

class TestExceededQuotaList(unittest.TestCase):
    """ExceededQuotaList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExceededQuotaList:
        """Test ExceededQuotaList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExceededQuotaList`
        """
        model = ExceededQuotaList()
        if include_optional:
            return ExceededQuotaList(
                data = [
                    taikunpycore.models.exceeded_quota_dto.ExceededQuotaDto(
                        cloud_id = 56, 
                        name = '', )
                    ],
                total_count = 56
            )
        else:
            return ExceededQuotaList(
                data = [
                    taikunpycore.models.exceeded_quota_dto.ExceededQuotaDto(
                        cloud_id = 56, 
                        name = '', )
                    ],
                total_count = 56,
        )
        """

    def testExceededQuotaList(self):
        """Test ExceededQuotaList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
