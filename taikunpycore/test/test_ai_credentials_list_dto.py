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

from taikunpycore.models.ai_credentials_list_dto import AiCredentialsListDto

class TestAiCredentialsListDto(unittest.TestCase):
    """AiCredentialsListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AiCredentialsListDto:
        """Test AiCredentialsListDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AiCredentialsListDto`
        """
        model = AiCredentialsListDto()
        if include_optional:
            return AiCredentialsListDto(
                id = 56,
                url = '',
                name = '',
                type = 'Taikun',
                organization_id = 56,
                organization_name = '',
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
                is_default = True
            )
        else:
            return AiCredentialsListDto(
                id = 56,
                url = '',
                name = '',
                type = 'Taikun',
                organization_id = 56,
                organization_name = '',
                projects = [
                    taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                        id = 56, 
                        name = '', )
                    ],
                is_default = True,
        )
        """

    def testAiCredentialsListDto(self):
        """Test AiCredentialsListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
