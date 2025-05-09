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

from taikunpycore.models.catalog_app_list import CatalogAppList

class TestCatalogAppList(unittest.TestCase):
    """CatalogAppList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CatalogAppList:
        """Test CatalogAppList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CatalogAppList`
        """
        model = CatalogAppList()
        if include_optional:
            return CatalogAppList(
                data = [
                    taikunpycore.models.catalog_app_list_dto.CatalogAppListDto(
                        catalog_app_id = 56, 
                        name = '', 
                        repo_id = 56, 
                        repo_name = '', 
                        catalog_id = 56, 
                        catalog_name = '', 
                        package_id = '', 
                        version = '', 
                        logo_image_id = '', 
                        is_locked = True, 
                        app_version = '', 
                        description = '', 
                        security_report_summary = taikunpycore.models.security_report_summary.SecurityReportSummary(
                            low = 56, 
                            high = 56, 
                            medium = 56, 
                            unknown = 56, 
                            critical = 56, ), 
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
                        stars = 56, 
                        installed_instance_count = 56, )
                    ],
                total_count = 56
            )
        else:
            return CatalogAppList(
        )
        """

    def testCatalogAppList(self):
        """Test CatalogAppList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
