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

from taikunpycore.models.bind_image_to_project_command import BindImageToProjectCommand

class TestBindImageToProjectCommand(unittest.TestCase):
    """BindImageToProjectCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BindImageToProjectCommand:
        """Test BindImageToProjectCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BindImageToProjectCommand`
        """
        model = BindImageToProjectCommand()
        if include_optional:
            return BindImageToProjectCommand(
                project_id = 56,
                images = [
                    ''
                    ]
            )
        else:
            return BindImageToProjectCommand(
        )
        """

    def testBindImageToProjectCommand(self):
        """Test BindImageToProjectCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
