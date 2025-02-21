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

from taikunpycore.models.flavors_list_dto import FlavorsListDto

class TestFlavorsListDto(unittest.TestCase):
    """FlavorsListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlavorsListDto:
        """Test FlavorsListDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlavorsListDto`
        """
        model = FlavorsListDto()
        if include_optional:
            return FlavorsListDto(
                ram = 1.337,
                cpu = 56,
                name = '',
                description = None,
                max_data_disk_count = 1.337
            )
        else:
            return FlavorsListDto(
                ram = 1.337,
                cpu = 56,
                name = '',
                description = None,
                max_data_disk_count = 1.337,
        )
        """

    def testFlavorsListDto(self):
        """Test FlavorsListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
