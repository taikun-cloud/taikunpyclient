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

from taikunpycore.models.check_s3_command import CheckS3Command

class TestCheckS3Command(unittest.TestCase):
    """CheckS3Command unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckS3Command:
        """Test CheckS3Command
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckS3Command`
        """
        model = CheckS3Command()
        if include_optional:
            return CheckS3Command(
                s3_access_key_id = '',
                s3_secret_key = '',
                s3_endpoint = '',
                s3_region = ''
            )
        else:
            return CheckS3Command(
        )
        """

    def testCheckS3Command(self):
        """Test CheckS3Command"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
