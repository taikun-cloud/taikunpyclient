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

from taikunpycore.models.admin_users_list import AdminUsersList

class TestAdminUsersList(unittest.TestCase):
    """AdminUsersList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminUsersList:
        """Test AdminUsersList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminUsersList`
        """
        model = AdminUsersList()
        if include_optional:
            return AdminUsersList(
                data = [
                    taikunpycore.models.admin_users_response_data.AdminUsersResponseData(
                        id = '', 
                        name = '', 
                        email = '', 
                        role = 'Admin', 
                        organization_name = '', 
                        owner = True, 
                        csm = True, )
                    ],
                total_count = 56
            )
        else:
            return AdminUsersList(
                data = [
                    taikunpycore.models.admin_users_response_data.AdminUsersResponseData(
                        id = '', 
                        name = '', 
                        email = '', 
                        role = 'Admin', 
                        organization_name = '', 
                        owner = True, 
                        csm = True, )
                    ],
                total_count = 56,
        )
        """

    def testAdminUsersList(self):
        """Test AdminUsersList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
