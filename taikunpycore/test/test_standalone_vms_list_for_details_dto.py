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

from taikunpycore.models.standalone_vms_list_for_details_dto import StandaloneVmsListForDetailsDto

class TestStandaloneVmsListForDetailsDto(unittest.TestCase):
    """StandaloneVmsListForDetailsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandaloneVmsListForDetailsDto:
        """Test StandaloneVmsListForDetailsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandaloneVmsListForDetailsDto`
        """
        model = StandaloneVmsListForDetailsDto()
        if include_optional:
            return StandaloneVmsListForDetailsDto(
                id = 56,
                name = '',
                image_name = '',
                image_id = '',
                status = '',
                cloud_init = '',
                volume_type = '',
                volume_size = 56,
                created_at = '',
                created_by = '',
                last_modified = '',
                last_modified_by = '',
                ssh_public_key = '',
                current_flavor = '',
                target_flavor = '',
                public_ip_enabled = True,
                public_ip = '',
                hypervisor = '',
                hypervisor_id = '',
                ip_address = '',
                spot_price = 1.337,
                spot_instance = True,
                availability_zone = '',
                action_buttons = taikunpycore.models.standalone_visibility_dto.StandaloneVisibilityDto(
                    show_status = True, 
                    show_console = True, 
                    shelve = True, 
                    unshelve = True, 
                    start = True, 
                    stop = True, 
                    reboot = True, ),
                is_windows = True,
                disks = [
                    taikunpycore.models.stand_alone_vm_disk_for_details_dto.StandAloneVmDiskForDetailsDto(
                        id = 56, 
                        name = '', 
                        current_size = 56, 
                        target_size = 56, 
                        volume_type = '', 
                        device_name = '', 
                        lun_id = '', 
                        status = 'Deleting', )
                    ],
                stand_alone_meta_datas = [
                    taikunpycore.models.stand_alone_meta_data_dto_for_vm.StandAloneMetaDataDtoForVm(
                        id = 56, 
                        key = '', 
                        value = '', )
                    ],
                profile = taikunpycore.models.stand_alone_profile_for_details_dto.StandAloneProfileForDetailsDto(
                    id = 56, 
                    name = '', 
                    public_key = '', 
                    security_groups = [
                        taikunpycore.models.stand_alone_profile_security_group_for_details_dto.StandAloneProfileSecurityGroupForDetailsDto(
                            id = 56, 
                            name = '', 
                            protocol = '', 
                            port_min_range = 56, 
                            port_max_range = 56, 
                            remote_ip_prefix = '', 
                            is_rdp_port_enabled = True, )
                        ], )
            )
        else:
            return StandaloneVmsListForDetailsDto(
                id = 56,
                name = '',
                image_name = '',
                image_id = '',
                status = '',
                cloud_init = '',
                volume_type = '',
                volume_size = 56,
                created_at = '',
                created_by = '',
                last_modified = '',
                last_modified_by = '',
                ssh_public_key = '',
                current_flavor = '',
                target_flavor = '',
                public_ip_enabled = True,
                public_ip = '',
                hypervisor = '',
                hypervisor_id = '',
                ip_address = '',
                spot_price = 1.337,
                spot_instance = True,
                availability_zone = '',
                action_buttons = taikunpycore.models.standalone_visibility_dto.StandaloneVisibilityDto(
                    show_status = True, 
                    show_console = True, 
                    shelve = True, 
                    unshelve = True, 
                    start = True, 
                    stop = True, 
                    reboot = True, ),
                is_windows = True,
                disks = [
                    taikunpycore.models.stand_alone_vm_disk_for_details_dto.StandAloneVmDiskForDetailsDto(
                        id = 56, 
                        name = '', 
                        current_size = 56, 
                        target_size = 56, 
                        volume_type = '', 
                        device_name = '', 
                        lun_id = '', 
                        status = 'Deleting', )
                    ],
                stand_alone_meta_datas = [
                    taikunpycore.models.stand_alone_meta_data_dto_for_vm.StandAloneMetaDataDtoForVm(
                        id = 56, 
                        key = '', 
                        value = '', )
                    ],
                profile = taikunpycore.models.stand_alone_profile_for_details_dto.StandAloneProfileForDetailsDto(
                    id = 56, 
                    name = '', 
                    public_key = '', 
                    security_groups = [
                        taikunpycore.models.stand_alone_profile_security_group_for_details_dto.StandAloneProfileSecurityGroupForDetailsDto(
                            id = 56, 
                            name = '', 
                            protocol = '', 
                            port_min_range = 56, 
                            port_max_range = 56, 
                            remote_ip_prefix = '', 
                            is_rdp_port_enabled = True, )
                        ], ),
        )
        """

    def testStandaloneVmsListForDetailsDto(self):
        """Test StandaloneVmsListForDetailsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
