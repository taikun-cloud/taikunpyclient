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

from taikunpycore.models.bound_images_for_projects_list_dto import BoundImagesForProjectsListDto

class TestBoundImagesForProjectsListDto(unittest.TestCase):
    """BoundImagesForProjectsListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BoundImagesForProjectsListDto:
        """Test BoundImagesForProjectsListDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BoundImagesForProjectsListDto`
        """
        model = BoundImagesForProjectsListDto()
        if include_optional:
            return BoundImagesForProjectsListDto(
                id = 56,
                name = '',
                project_id = 56,
                project_name = '',
                size = 1.337,
                image_id = '',
                cloud_id = 56,
                is_windows = True,
                cloud_type = 'NONE'
            )
        else:
            return BoundImagesForProjectsListDto(
                id = 56,
                name = '',
                project_id = 56,
                project_name = '',
                size = 1.337,
                image_id = '',
                cloud_id = 56,
                is_windows = True,
                cloud_type = 'NONE',
        )
        """

    def testBoundImagesForProjectsListDto(self):
        """Test BoundImagesForProjectsListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
