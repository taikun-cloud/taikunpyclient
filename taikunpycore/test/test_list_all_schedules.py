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

from taikunpycore.models.list_all_schedules import ListAllSchedules

class TestListAllSchedules(unittest.TestCase):
    """ListAllSchedules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAllSchedules:
        """Test ListAllSchedules
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllSchedules`
        """
        model = ListAllSchedules()
        if include_optional:
            return ListAllSchedules(
                data = [
                    taikunpycore.models.c_schedule_dto.CScheduleDto(
                        status = taikunpycore.models.status.Status(
                            last_backup = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            phase = '', ), 
                        metadata_name = '', 
                        namespace = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        schedule = '', 
                        ttl = '', 
                        last_backup = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        phase = '', 
                        excluded_namespaces = [
                            ''
                            ], 
                        included_namespaces = [
                            ''
                            ], )
                    ],
                total_count = 56
            )
        else:
            return ListAllSchedules(
                data = [
                    taikunpycore.models.c_schedule_dto.CScheduleDto(
                        status = taikunpycore.models.status.Status(
                            last_backup = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            phase = '', ), 
                        metadata_name = '', 
                        namespace = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        schedule = '', 
                        ttl = '', 
                        last_backup = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        phase = '', 
                        excluded_namespaces = [
                            ''
                            ], 
                        included_namespaces = [
                            ''
                            ], )
                    ],
                total_count = 56,
        )
        """

    def testListAllSchedules(self):
        """Test ListAllSchedules"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
