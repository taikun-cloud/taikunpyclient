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

from taikunpycore.models.openstack_subnet_list_query import OpenstackSubnetListQuery

class TestOpenstackSubnetListQuery(unittest.TestCase):
    """OpenstackSubnetListQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenstackSubnetListQuery:
        """Test OpenstackSubnetListQuery
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenstackSubnetListQuery`
        """
        model = OpenstackSubnetListQuery()
        if include_optional:
            return OpenstackSubnetListQuery(
                open_stack_user = '',
                open_stack_password = '',
                open_stack_url = '',
                open_stack_project = '',
                open_stack_project_id = '',
                open_stack_domain = '',
                open_stack_region = '',
                application_cred_enabled = True
            )
        else:
            return OpenstackSubnetListQuery(
        )
        """

    def testOpenstackSubnetListQuery(self):
        """Test OpenstackSubnetListQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
