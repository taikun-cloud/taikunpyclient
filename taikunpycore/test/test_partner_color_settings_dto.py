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

from taikunpycore.models.partner_color_settings_dto import PartnerColorSettingsDto

class TestPartnerColorSettingsDto(unittest.TestCase):
    """PartnerColorSettingsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartnerColorSettingsDto:
        """Test PartnerColorSettingsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartnerColorSettingsDto`
        """
        model = PartnerColorSettingsDto()
        if include_optional:
            return PartnerColorSettingsDto(
                bg = '',
                bg_collapsed_sub_item = '',
                item_text = '',
                item_bg = '',
                item_bg_hover = '',
                item_text_active = '',
                item_bg_active = '',
                item_bg_active_hover = ''
            )
        else:
            return PartnerColorSettingsDto(
                bg = '',
                bg_collapsed_sub_item = '',
                item_text = '',
                item_bg = '',
                item_bg_hover = '',
                item_text_active = '',
                item_bg_active = '',
                item_bg_active_hover = '',
        )
        """

    def testPartnerColorSettingsDto(self):
        """Test PartnerColorSettingsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
