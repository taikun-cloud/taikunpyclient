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

from taikunpycore.models.stand_alone_vm_disk_for_details_dto import StandAloneVmDiskForDetailsDto

class TestStandAloneVmDiskForDetailsDto(unittest.TestCase):
    """StandAloneVmDiskForDetailsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandAloneVmDiskForDetailsDto:
        """Test StandAloneVmDiskForDetailsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandAloneVmDiskForDetailsDto`
        """
        model = StandAloneVmDiskForDetailsDto()
        if include_optional:
            return StandAloneVmDiskForDetailsDto(
                id = 56,
                name = '',
                current_size = 56,
                target_size = 56,
                volume_type = '',
                device_name = '',
                lun_id = '',
                status = 'Deleting'
            )
        else:
            return StandAloneVmDiskForDetailsDto(
                id = 56,
                name = '',
                current_size = 56,
                target_size = 56,
                volume_type = '',
                device_name = '',
                lun_id = '',
                status = 'Deleting',
        )
        """

    def testStandAloneVmDiskForDetailsDto(self):
        """Test StandAloneVmDiskForDetailsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
