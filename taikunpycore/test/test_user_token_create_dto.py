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

from taikunpycore.models.user_token_create_dto import UserTokenCreateDto

class TestUserTokenCreateDto(unittest.TestCase):
    """UserTokenCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserTokenCreateDto:
        """Test UserTokenCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserTokenCreateDto`
        """
        model = UserTokenCreateDto()
        if include_optional:
            return UserTokenCreateDto(
                access_key = '',
                secret_key = ''
            )
        else:
            return UserTokenCreateDto(
        )
        """

    def testUserTokenCreateDto(self):
        """Test UserTokenCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
