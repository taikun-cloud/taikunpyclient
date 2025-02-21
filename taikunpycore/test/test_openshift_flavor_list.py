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

from taikunpycore.models.openshift_flavor_list import OpenshiftFlavorList

class TestOpenshiftFlavorList(unittest.TestCase):
    """OpenshiftFlavorList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenshiftFlavorList:
        """Test OpenshiftFlavorList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenshiftFlavorList`
        """
        model = OpenshiftFlavorList()
        if include_optional:
            return OpenshiftFlavorList(
                data = [
                    taikunpycore.models.openshift_flavor_data.OpenshiftFlavorData(
                        name = '', 
                        cpu = 56, 
                        ram = 1.337, )
                    ],
                total_count = 56
            )
        else:
            return OpenshiftFlavorList(
                data = [
                    taikunpycore.models.openshift_flavor_data.OpenshiftFlavorData(
                        name = '', 
                        cpu = 56, 
                        ram = 1.337, )
                    ],
                total_count = 56,
        )
        """

    def testOpenshiftFlavorList(self):
        """Test OpenshiftFlavorList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
