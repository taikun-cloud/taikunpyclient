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

from taikunpycore.models.catalog_app_params_dto import CatalogAppParamsDto

class TestCatalogAppParamsDto(unittest.TestCase):
    """CatalogAppParamsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CatalogAppParamsDto:
        """Test CatalogAppParamsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CatalogAppParamsDto`
        """
        model = CatalogAppParamsDto()
        if include_optional:
            return CatalogAppParamsDto(
                key = '',
                value = '',
                is_editable_when_installing = True,
                is_editable_after_installation = True,
                is_mandatory = True
            )
        else:
            return CatalogAppParamsDto(
        )
        """

    def testCatalogAppParamsDto(self):
        """Test CatalogAppParamsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
