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

from taikunpycore.api.kubernetes_profiles_api import KubernetesProfilesApi


class TestKubernetesProfilesApi(unittest.TestCase):
    """KubernetesProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KubernetesProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_kubernetesprofiles_create(self) -> None:
        """Test case for kubernetesprofiles_create

        Add kubernetes profile
        """
        pass

    def test_kubernetesprofiles_delete(self) -> None:
        """Test case for kubernetesprofiles_delete

        Delete kubernetes profile
        """
        pass

    def test_kubernetesprofiles_dropdown(self) -> None:
        """Test case for kubernetesprofiles_dropdown

        Retrieve all kubernetes profiles for organization
        """
        pass

    def test_kubernetesprofiles_list(self) -> None:
        """Test case for kubernetesprofiles_list

        Retrieve all kubernetes profiles
        """
        pass

    def test_kubernetesprofiles_lock_manager(self) -> None:
        """Test case for kubernetesprofiles_lock_manager

        Kubernetes profile lock/unlock
        """
        pass


if __name__ == '__main__':
    unittest.main()
