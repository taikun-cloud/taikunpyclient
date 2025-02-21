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

from taikunpycore.models.list_for_partners_dto import ListForPartnersDto

class TestListForPartnersDto(unittest.TestCase):
    """ListForPartnersDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListForPartnersDto:
        """Test ListForPartnersDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListForPartnersDto`
        """
        model = ListForPartnersDto()
        if include_optional:
            return ListForPartnersDto(
                id = 56,
                name = '',
                project_limit = 56,
                server_limit = 56,
                user_limit = 56,
                cloud_credential_limit = 56,
                monthly_price = 1.337,
                yearly_price = 1.337,
                tcu_price = 1.337,
                is_deprecated = True,
                currency = '',
                is_enterprise = True,
                partner = taikunpycore.models.partner_details_for_subscription.PartnerDetailsForSubscription(
                    name = '', 
                    logo = '', 
                    link = '', 
                    id = 56, ),
                exceeded_user = True,
                exceeded_project = True,
                exceeded_cloud_credential = True,
                exceeded_servers = True,
                is_active = True,
                is_yearly = True,
                trial_days = 56,
                description = '',
                is_demo = True
            )
        else:
            return ListForPartnersDto(
                id = 56,
                name = '',
                project_limit = 56,
                server_limit = 56,
                user_limit = 56,
                cloud_credential_limit = 56,
                monthly_price = 1.337,
                yearly_price = 1.337,
                tcu_price = 1.337,
                is_deprecated = True,
                currency = '',
                is_enterprise = True,
                partner = taikunpycore.models.partner_details_for_subscription.PartnerDetailsForSubscription(
                    name = '', 
                    logo = '', 
                    link = '', 
                    id = 56, ),
                exceeded_user = True,
                exceeded_project = True,
                exceeded_cloud_credential = True,
                exceeded_servers = True,
                is_active = True,
                is_yearly = True,
                trial_days = 56,
                description = '',
                is_demo = True,
        )
        """

    def testListForPartnersDto(self):
        """Test ListForPartnersDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
