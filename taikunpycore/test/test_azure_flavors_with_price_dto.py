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

from taikunpycore.models.azure_flavors_with_price_dto import AzureFlavorsWithPriceDto

class TestAzureFlavorsWithPriceDto(unittest.TestCase):
    """AzureFlavorsWithPriceDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureFlavorsWithPriceDto:
        """Test AzureFlavorsWithPriceDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureFlavorsWithPriceDto`
        """
        model = AzureFlavorsWithPriceDto()
        if include_optional:
            return AzureFlavorsWithPriceDto(
                name = '',
                windows_price = '',
                linux_price = '',
                windows_spot_price = '',
                linux_spot_price = '',
                cpu = 56,
                ram = 1.337,
                description = None,
                max_data_disk_count = 1.337
            )
        else:
            return AzureFlavorsWithPriceDto(
        )
        """

    def testAzureFlavorsWithPriceDto(self):
        """Test AzureFlavorsWithPriceDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
