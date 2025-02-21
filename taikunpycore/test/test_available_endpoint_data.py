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

from taikunpycore.models.available_endpoint_data import AvailableEndpointData

class TestAvailableEndpointData(unittest.TestCase):
    """AvailableEndpointData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvailableEndpointData:
        """Test AvailableEndpointData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvailableEndpointData`
        """
        model = AvailableEndpointData()
        if include_optional:
            return AvailableEndpointData(
                id = 56,
                path = '',
                method = '',
                description = '',
                controller = ''
            )
        else:
            return AvailableEndpointData(
        )
        """

    def testAvailableEndpointData(self):
        """Test AvailableEndpointData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
