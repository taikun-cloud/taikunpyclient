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

from taikunpycore.models.available_packages_dto import AvailablePackagesDto

class TestAvailablePackagesDto(unittest.TestCase):
    """AvailablePackagesDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvailablePackagesDto:
        """Test AvailablePackagesDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvailablePackagesDto`
        """
        model = AvailablePackagesDto()
        if include_optional:
            return AvailablePackagesDto(
                package_id = '',
                catalog_id = 56,
                catalog_app_id = 56,
                installed_instance_count = 56,
                name = '',
                normalized_name = '',
                logo_image_id = '',
                stars = 56,
                description = '',
                version = '',
                app_version = '',
                deprecated = True,
                signed = True,
                is_locked = True,
                security_report_summary = taikunpycore.models.security_report_summary.SecurityReportSummary(
                    low = 56, 
                    high = 56, 
                    medium = 56, 
                    unknown = 56, 
                    critical = 56, ),
                ts = '',
                repository = taikunpycore.models.repository.Repository(
                    url = '', 
                    kind = 56, 
                    name = '', 
                    official = True, 
                    repository_id = '', 
                    scanner_disabled = True, 
                    is_imported = True, 
                    organization_name = '', 
                    verified_publisher = True, 
                    organization_display_name = '', ),
                is_added = True
            )
        else:
            return AvailablePackagesDto(
        )
        """

    def testAvailablePackagesDto(self):
        """Test AvailablePackagesDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
