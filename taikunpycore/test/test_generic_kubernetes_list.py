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

from taikunpycore.models.generic_kubernetes_list import GenericKubernetesList

class TestGenericKubernetesList(unittest.TestCase):
    """GenericKubernetesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericKubernetesList:
        """Test GenericKubernetesList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericKubernetesList`
        """
        model = GenericKubernetesList()
        if include_optional:
            return GenericKubernetesList(
                data = [
                    taikunpycore.models.generic_kubernetes_list_dto.GenericKubernetesListDto(
                        id = 56, 
                        project_count = 56, 
                        is_locked = True, 
                        name = '', 
                        main_project = taikunpycore.models.main_project_dto.MainProjectDto(
                            id = 56, 
                            name = '', 
                            status = 'Null', ), 
                        associated_v_clusters = [
                            taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                                id = 56, 
                                name = '', )
                            ], 
                        created_by = '', 
                        created_at = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        is_default = True, 
                        organization_id = 56, 
                        organization_name = '', 
                        continent_name = '', )
                    ],
                total_count = 56
            )
        else:
            return GenericKubernetesList(
                data = [
                    taikunpycore.models.generic_kubernetes_list_dto.GenericKubernetesListDto(
                        id = 56, 
                        project_count = 56, 
                        is_locked = True, 
                        name = '', 
                        main_project = taikunpycore.models.main_project_dto.MainProjectDto(
                            id = 56, 
                            name = '', 
                            status = 'Null', ), 
                        associated_v_clusters = [
                            taikunpycore.models.common_dropdown_dto.CommonDropdownDto(
                                id = 56, 
                                name = '', )
                            ], 
                        created_by = '', 
                        created_at = '', 
                        last_modified = '', 
                        last_modified_by = '', 
                        is_default = True, 
                        organization_id = 56, 
                        organization_name = '', 
                        continent_name = '', )
                    ],
                total_count = 56,
        )
        """

    def testGenericKubernetesList(self):
        """Test GenericKubernetesList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
