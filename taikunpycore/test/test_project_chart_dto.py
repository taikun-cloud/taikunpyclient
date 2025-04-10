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

from taikunpycore.models.project_chart_dto import ProjectChartDto

class TestProjectChartDto(unittest.TestCase):
    """ProjectChartDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectChartDto:
        """Test ProjectChartDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectChartDto`
        """
        model = ProjectChartDto()
        if include_optional:
            return ProjectChartDto(
                succeeded = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ],
                updating = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ],
                total_count = 56,
                failed = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ],
                purging = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ],
                deleting = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ],
                importing = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ],
                failed_to_import = [
                    taikunpycore.models.project_common_record_dto.ProjectCommonRecordDto(
                        id = 56, 
                        name = '', 
                        expired_at = '', )
                    ]
            )
        else:
            return ProjectChartDto(
        )
        """

    def testProjectChartDto(self):
        """Test ProjectChartDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
