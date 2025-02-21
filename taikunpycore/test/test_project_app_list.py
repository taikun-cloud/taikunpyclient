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

from taikunpycore.models.project_app_list import ProjectAppList

class TestProjectAppList(unittest.TestCase):
    """ProjectAppList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectAppList:
        """Test ProjectAppList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectAppList`
        """
        model = ProjectAppList()
        if include_optional:
            return ProjectAppList(
                data = [
                    taikunpycore.models.instance_app_list_dto.InstanceAppListDto(
                        id = 56, 
                        name = '', 
                        namespace = '', 
                        status = 'None', 
                        version = '', 
                        catalog_id = 56, 
                        catalog_name = '', 
                        catalog_app_name = '', 
                        catalog_app_id = 56, 
                        app_repo_name = '', 
                        logo = '', 
                        auto_sync = True, 
                        created = '', 
                        created_by = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        project_id = 56, 
                        project_name = '', 
                        logs = '', )
                    ],
                total_count = 56
            )
        else:
            return ProjectAppList(
                data = [
                    taikunpycore.models.instance_app_list_dto.InstanceAppListDto(
                        id = 56, 
                        name = '', 
                        namespace = '', 
                        status = 'None', 
                        version = '', 
                        catalog_id = 56, 
                        catalog_name = '', 
                        catalog_app_name = '', 
                        catalog_app_id = 56, 
                        app_repo_name = '', 
                        logo = '', 
                        auto_sync = True, 
                        created = '', 
                        created_by = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        project_id = 56, 
                        project_name = '', 
                        logs = '', )
                    ],
                total_count = 56,
        )
        """

    def testProjectAppList(self):
        """Test ProjectAppList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
