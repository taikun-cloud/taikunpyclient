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

from taikunpycore.models.admin_projects_list import AdminProjectsList

class TestAdminProjectsList(unittest.TestCase):
    """AdminProjectsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminProjectsList:
        """Test AdminProjectsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminProjectsList`
        """
        model = AdminProjectsList()
        if include_optional:
            return AdminProjectsList(
                data = [
                    taikunpycore.models.admin_projects_response_data.AdminProjectsResponseData(
                        id = 56, 
                        name = '', 
                        organization_name = '', 
                        is_locked = True, 
                        kubernetes_current_version = '', 
                        kubespray_current_version = '', 
                        status = 'Null', 
                        servers_count = 56, 
                        tcu = 56, 
                        created_at = '', 
                        cloud_type = 'NONE', )
                    ],
                total_count = 56
            )
        else:
            return AdminProjectsList(
                data = [
                    taikunpycore.models.admin_projects_response_data.AdminProjectsResponseData(
                        id = 56, 
                        name = '', 
                        organization_name = '', 
                        is_locked = True, 
                        kubernetes_current_version = '', 
                        kubespray_current_version = '', 
                        status = 'Null', 
                        servers_count = 56, 
                        tcu = 56, 
                        created_at = '', 
                        cloud_type = 'NONE', )
                    ],
                total_count = 56,
        )
        """

    def testAdminProjectsList(self):
        """Test AdminProjectsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
