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

from taikunpycore.models.stand_alone_profiles import StandAloneProfiles

class TestStandAloneProfiles(unittest.TestCase):
    """StandAloneProfiles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandAloneProfiles:
        """Test StandAloneProfiles
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandAloneProfiles`
        """
        model = StandAloneProfiles()
        if include_optional:
            return StandAloneProfiles(
                data = [
                    taikunpycore.models.stand_alone_profiles_list_dto.StandAloneProfilesListDto(
                        id = 56, 
                        name = '', 
                        public_key = '', 
                        is_locked = True, 
                        standalone_vms = [
                            taikunpycore.models.stand_alone_vm_small_detail_dto.StandAloneVmSmallDetailDto(
                                id = 56, 
                                name = '', 
                                project_id = 56, )
                            ], 
                        organization_id = 56, 
                        organization_name = '', 
                        partner_logo = '', 
                        created_at = '', )
                    ],
                total_count = 56
            )
        else:
            return StandAloneProfiles(
                data = [
                    taikunpycore.models.stand_alone_profiles_list_dto.StandAloneProfilesListDto(
                        id = 56, 
                        name = '', 
                        public_key = '', 
                        is_locked = True, 
                        standalone_vms = [
                            taikunpycore.models.stand_alone_vm_small_detail_dto.StandAloneVmSmallDetailDto(
                                id = 56, 
                                name = '', 
                                project_id = 56, )
                            ], 
                        organization_id = 56, 
                        organization_name = '', 
                        partner_logo = '', 
                        created_at = '', )
                    ],
                total_count = 56,
        )
        """

    def testStandAloneProfiles(self):
        """Test StandAloneProfiles"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
