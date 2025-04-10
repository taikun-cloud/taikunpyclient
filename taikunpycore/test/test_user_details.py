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

from taikunpycore.models.user_details import UserDetails

class TestUserDetails(unittest.TestCase):
    """UserDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDetails:
        """Test UserDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDetails`
        """
        model = UserDetails()
        if include_optional:
            return UserDetails(
                data = taikunpycore.models.user_for_list_dto.UserForListDto(
                    id = '', 
                    username = '', 
                    organization_name = '', 
                    has_customer_id = True, 
                    has_payment_method = True, 
                    organization_id = 56, 
                    role = 'Admin', 
                    role_name = '', 
                    email = '', 
                    display_name = '', 
                    created_at = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_email_confirmed = True, 
                    is_email_notification_enabled = True, 
                    is_forced_to_reset_password = True, 
                    is_csm = True, 
                    is_eligible_update_subscription = True, 
                    is_locked = True, 
                    is_approved_by_partner = True, 
                    owner = True, 
                    is_read_only = True, 
                    has_repo = True, 
                    is_new_organization = True, 
                    is2_fa_enabled = True, 
                    last_login_at = '', 
                    bound_projects = [
                        taikunpycore.models.project_dto.ProjectDto(
                            project_id = 56, 
                            project_name = '', )
                        ], 
                    partner = taikunpycore.models.partner_details_for_user_dto.PartnerDetailsForUserDto(
                        name = '', 
                        logo = '', 
                        link = '', 
                        domain = '', 
                        id = 56, ), ),
                is_maintenance_mode_enabled = True,
                trial_days = 56
            )
        else:
            return UserDetails(
                data = taikunpycore.models.user_for_list_dto.UserForListDto(
                    id = '', 
                    username = '', 
                    organization_name = '', 
                    has_customer_id = True, 
                    has_payment_method = True, 
                    organization_id = 56, 
                    role = 'Admin', 
                    role_name = '', 
                    email = '', 
                    display_name = '', 
                    created_at = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_email_confirmed = True, 
                    is_email_notification_enabled = True, 
                    is_forced_to_reset_password = True, 
                    is_csm = True, 
                    is_eligible_update_subscription = True, 
                    is_locked = True, 
                    is_approved_by_partner = True, 
                    owner = True, 
                    is_read_only = True, 
                    has_repo = True, 
                    is_new_organization = True, 
                    is2_fa_enabled = True, 
                    last_login_at = '', 
                    bound_projects = [
                        taikunpycore.models.project_dto.ProjectDto(
                            project_id = 56, 
                            project_name = '', )
                        ], 
                    partner = taikunpycore.models.partner_details_for_user_dto.PartnerDetailsForUserDto(
                        name = '', 
                        logo = '', 
                        link = '', 
                        domain = '', 
                        id = 56, ), ),
                is_maintenance_mode_enabled = True,
                trial_days = 56,
        )
        """

    def testUserDetails(self):
        """Test UserDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
