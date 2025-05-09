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

from taikunpycore.api.project_templates_api import ProjectTemplatesApi


class TestProjectTemplatesApi(unittest.TestCase):
    """ProjectTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_project_templates_create(self) -> None:
        """Test case for project_templates_create

        Create project from template
        """
        pass

    def test_project_templates_delete(self) -> None:
        """Test case for project_templates_delete

        Delete project template by Id
        """
        pass

    def test_project_templates_dropdown(self) -> None:
        """Test case for project_templates_dropdown

        Retrieve project template by organization Id
        """
        pass

    def test_project_templates_list(self) -> None:
        """Test case for project_templates_list

        Retrieve all project templates
        """
        pass


if __name__ == '__main__':
    unittest.main()
