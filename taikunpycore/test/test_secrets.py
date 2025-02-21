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

from taikunpycore.models.secrets import Secrets

class TestSecrets(unittest.TestCase):
    """Secrets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Secrets:
        """Test Secrets
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Secrets`
        """
        model = Secrets()
        if include_optional:
            return Secrets(
                data = [
                    taikunpycore.models.secret_dto.SecretDto(
                        metadata_name = '', 
                        namespace = '', 
                        age = '', )
                    ],
                total_count = 56
            )
        else:
            return Secrets(
                data = [
                    taikunpycore.models.secret_dto.SecretDto(
                        metadata_name = '', 
                        namespace = '', 
                        age = '', )
                    ],
                total_count = 56,
        )
        """

    def testSecrets(self):
        """Test Secrets"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
