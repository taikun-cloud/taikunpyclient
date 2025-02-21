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

from taikunpycore.models.kubernetes_cron_jobs_list import KubernetesCronJobsList

class TestKubernetesCronJobsList(unittest.TestCase):
    """KubernetesCronJobsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KubernetesCronJobsList:
        """Test KubernetesCronJobsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KubernetesCronJobsList`
        """
        model = KubernetesCronJobsList()
        if include_optional:
            return KubernetesCronJobsList(
                data = [
                    taikunpycore.models.kubernetes_cron_job_dto.KubernetesCronJobDto(
                        metadata_name = '', 
                        last_schedule = '', 
                        suspend = True, 
                        schedule = '', 
                        namespace = '', 
                        age = '', )
                    ],
                total_count = 56
            )
        else:
            return KubernetesCronJobsList(
                data = [
                    taikunpycore.models.kubernetes_cron_job_dto.KubernetesCronJobDto(
                        metadata_name = '', 
                        last_schedule = '', 
                        suspend = True, 
                        schedule = '', 
                        namespace = '', 
                        age = '', )
                    ],
                total_count = 56,
        )
        """

    def testKubernetesCronJobsList(self):
        """Test KubernetesCronJobsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
