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

from taikunpycore.models.unbind_project_from_project_group_command import UnbindProjectFromProjectGroupCommand

class TestUnbindProjectFromProjectGroupCommand(unittest.TestCase):
    """UnbindProjectFromProjectGroupCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnbindProjectFromProjectGroupCommand:
        """Test UnbindProjectFromProjectGroupCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnbindProjectFromProjectGroupCommand`
        """
        model = UnbindProjectFromProjectGroupCommand()
        if include_optional:
            return UnbindProjectFromProjectGroupCommand(
                project_group_id = 56,
                project_ids = [
                    56
                    ]
            )
        else:
            return UnbindProjectFromProjectGroupCommand(
        )
        """

    def testUnbindProjectFromProjectGroupCommand(self):
        """Test UnbindProjectFromProjectGroupCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
