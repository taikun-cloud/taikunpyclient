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

from taikunpycore.api.project_deployment_api import ProjectDeploymentApi


class TestProjectDeploymentApi(unittest.TestCase):
    """ProjectDeploymentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectDeploymentApi()

    def tearDown(self) -> None:
        pass

    def test_project_deployment_commit(self) -> None:
        """Test case for project_deployment_commit

        Commit
        """
        pass

    def test_project_deployment_commit_vm(self) -> None:
        """Test case for project_deployment_commit_vm

        Commit
        """
        pass

    def test_project_deployment_completed(self) -> None:
        """Test case for project_deployment_completed

        Update project fields
        """
        pass

    def test_project_deployment_delete(self) -> None:
        """Test case for project_deployment_delete

        Delete
        """
        pass

    def test_project_deployment_delete_vm_disks(self) -> None:
        """Test case for project_deployment_delete_vm_disks

        Delete vm disks
        """
        pass

    def test_project_deployment_delete_vms(self) -> None:
        """Test case for project_deployment_delete_vms

        Delete vms
        """
        pass

    def test_project_deployment_disable_ai(self) -> None:
        """Test case for project_deployment_disable_ai

        Disable ai
        """
        pass

    def test_project_deployment_disable_backup(self) -> None:
        """Test case for project_deployment_disable_backup

        Disable backup
        """
        pass

    def test_project_deployment_disable_monitoring(self) -> None:
        """Test case for project_deployment_disable_monitoring

        Disable monitoring
        """
        pass

    def test_project_deployment_disable_opa(self) -> None:
        """Test case for project_deployment_disable_opa

        Disable opa
        """
        pass

    def test_project_deployment_enable_ai(self) -> None:
        """Test case for project_deployment_enable_ai

        Enable ai
        """
        pass

    def test_project_deployment_enable_backup(self) -> None:
        """Test case for project_deployment_enable_backup

        Enable backup
        """
        pass

    def test_project_deployment_enable_monitoring(self) -> None:
        """Test case for project_deployment_enable_monitoring

        Enable monitoring
        """
        pass

    def test_project_deployment_enable_opa(self) -> None:
        """Test case for project_deployment_enable_opa

        Enable opa
        """
        pass

    def test_project_deployment_import_cluster(self) -> None:
        """Test case for project_deployment_import_cluster

        Import cluster
        """
        pass

    def test_project_deployment_repair(self) -> None:
        """Test case for project_deployment_repair

        Repair
        """
        pass

    def test_project_deployment_repair_vm(self) -> None:
        """Test case for project_deployment_repair_vm

        Repair Vm
        """
        pass

    def test_project_deployment_tofu_migrate(self) -> None:
        """Test case for project_deployment_tofu_migrate

        Tofu migrate
        """
        pass

    def test_project_deployment_update(self) -> None:
        """Test case for project_deployment_update

        Update stage of project
        """
        pass

    def test_project_deployment_upgrade(self) -> None:
        """Test case for project_deployment_upgrade

        Upgrade the project's Kubernetes to the next available version. Project must be READY.
        """
        pass


if __name__ == '__main__':
    unittest.main()
