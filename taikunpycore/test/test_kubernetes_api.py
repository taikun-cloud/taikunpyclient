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

from taikunpycore.api.kubernetes_api import KubernetesApi


class TestKubernetesApi(unittest.TestCase):
    """KubernetesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KubernetesApi()

    def tearDown(self) -> None:
        pass

    def test_kubernetes_add_k8s_alert(self) -> None:
        """Test case for kubernetes_add_k8s_alert

        Add k8s alert
        """
        pass

    def test_kubernetes_add_k8s_events(self) -> None:
        """Test case for kubernetes_add_k8s_events

        Add k8s event
        """
        pass

    def test_kubernetes_alert_list(self) -> None:
        """Test case for kubernetes_alert_list

        Retrieve a list of alerts for project
        """
        pass

    def test_kubernetes_cli(self) -> None:
        """Test case for kubernetes_cli

        Execute k8s web socket namespaced pod
        """
        pass

    def test_kubernetes_config_map_list(self) -> None:
        """Test case for kubernetes_config_map_list

        Retrieve a list of k8s config map for all namespaces
        """
        pass

    def test_kubernetes_crd_list(self) -> None:
        """Test case for kubernetes_crd_list

        Retrieve a list of crd
        """
        pass

    def test_kubernetes_create_resource(self) -> None:
        """Test case for kubernetes_create_resource

        Create kubernetes resource
        """
        pass

    def test_kubernetes_cron_job_list(self) -> None:
        """Test case for kubernetes_cron_job_list

        Retrieve a list of k8s cron jobs for all namespaces
        """
        pass

    def test_kubernetes_cronjob_actions(self) -> None:
        """Test case for kubernetes_cronjob_actions

        Cronjob actions
        """
        pass

    def test_kubernetes_daemon_set_list(self) -> None:
        """Test case for kubernetes_daemon_set_list

        Retrieve list of k8s daemonset
        """
        pass

    def test_kubernetes_daemonset_actions(self) -> None:
        """Test case for kubernetes_daemonset_actions

        Daemonset actions
        """
        pass

    def test_kubernetes_dashboard_list(self) -> None:
        """Test case for kubernetes_dashboard_list

        Retrieve a list of crd
        """
        pass

    def test_kubernetes_delete_resource(self) -> None:
        """Test case for kubernetes_delete_resource

        Delete kubernetes resource
        """
        pass

    def test_kubernetes_deployment_actions(self) -> None:
        """Test case for kubernetes_deployment_actions

        Deployment actions
        """
        pass

    def test_kubernetes_deployment_list(self) -> None:
        """Test case for kubernetes_deployment_list

        Retrieve a list of k8s deployment for all namespaces
        """
        pass

    def test_kubernetes_describe_config_map(self) -> None:
        """Test case for kubernetes_describe_config_map

        Describe configmap
        """
        pass

    def test_kubernetes_describe_crd(self) -> None:
        """Test case for kubernetes_describe_crd

        Describe crd
        """
        pass

    def test_kubernetes_describe_cronjob(self) -> None:
        """Test case for kubernetes_describe_cronjob

        Describe cronjob
        """
        pass

    def test_kubernetes_describe_daemon_set(self) -> None:
        """Test case for kubernetes_describe_daemon_set

        Describe daemonset
        """
        pass

    def test_kubernetes_describe_deployment(self) -> None:
        """Test case for kubernetes_describe_deployment

        Describe deployment
        """
        pass

    def test_kubernetes_describe_ingress(self) -> None:
        """Test case for kubernetes_describe_ingress

        Describe ingress
        """
        pass

    def test_kubernetes_describe_job(self) -> None:
        """Test case for kubernetes_describe_job

        Describe job
        """
        pass

    def test_kubernetes_describe_network_policy(self) -> None:
        """Test case for kubernetes_describe_network_policy

        Describe network policy
        """
        pass

    def test_kubernetes_describe_node(self) -> None:
        """Test case for kubernetes_describe_node

        Describe node
        """
        pass

    def test_kubernetes_describe_pdb(self) -> None:
        """Test case for kubernetes_describe_pdb

        Describe pdb
        """
        pass

    def test_kubernetes_describe_pod(self) -> None:
        """Test case for kubernetes_describe_pod

        Describe pod
        """
        pass

    def test_kubernetes_describe_pvc(self) -> None:
        """Test case for kubernetes_describe_pvc

        Describe pvc
        """
        pass

    def test_kubernetes_describe_resource(self) -> None:
        """Test case for kubernetes_describe_resource

        Describe kubernetes resource
        """
        pass

    def test_kubernetes_describe_secret(self) -> None:
        """Test case for kubernetes_describe_secret

        Describe secret
        """
        pass

    def test_kubernetes_describe_service(self) -> None:
        """Test case for kubernetes_describe_service

        Describe service
        """
        pass

    def test_kubernetes_describe_storage_class(self) -> None:
        """Test case for kubernetes_describe_storage_class

        Describe storage class
        """
        pass

    def test_kubernetes_describe_sts(self) -> None:
        """Test case for kubernetes_describe_sts

        Describe stateful set
        """
        pass

    def test_kubernetes_download(self) -> None:
        """Test case for kubernetes_download

        Download kube config file
        """
        pass

    def test_kubernetes_download_manifest(self) -> None:
        """Test case for kubernetes_download_manifest

        Download manifest
        """
        pass

    def test_kubernetes_export(self) -> None:
        """Test case for kubernetes_export

        Export
        """
        pass

    def test_kubernetes_forbidden_namespaces(self) -> None:
        """Test case for kubernetes_forbidden_namespaces

        Forbidden namespaces for k8s actions
        """
        pass

    def test_kubernetes_get_supported_list(self) -> None:
        """Test case for kubernetes_get_supported_list

        Retrieve Taikun supported kubernetes versions
        """
        pass

    def test_kubernetes_helm_release_list(self) -> None:
        """Test case for kubernetes_helm_release_list

        Retrieve a list of k8s helm releases for all namespaces
        """
        pass

    def test_kubernetes_ingress_classes(self) -> None:
        """Test case for kubernetes_ingress_classes

        List of ingress classes
        """
        pass

    def test_kubernetes_ingress_list(self) -> None:
        """Test case for kubernetes_ingress_list

        Retrieve a list of k8s ingress for all namespaces
        """
        pass

    def test_kubernetes_interactive_shell(self) -> None:
        """Test case for kubernetes_interactive_shell

        Produce interactive shell command
        """
        pass

    def test_kubernetes_jobs_list(self) -> None:
        """Test case for kubernetes_jobs_list

        Retrieve a list of k8s jobs for all namespaces
        """
        pass

    def test_kubernetes_kill_pod(self) -> None:
        """Test case for kubernetes_kill_pod

        Kill the pod
        """
        pass

    def test_kubernetes_kube_config(self) -> None:
        """Test case for kubernetes_kube_config

        Retrieve kube config file
        """
        pass

    def test_kubernetes_namespace_list(self) -> None:
        """Test case for kubernetes_namespace_list

        Retrieve kube config file
        """
        pass

    def test_kubernetes_network_policy_list(self) -> None:
        """Test case for kubernetes_network_policy_list

        Retrieve a list of k8s network-policies for all namespaces
        """
        pass

    def test_kubernetes_node_actions(self) -> None:
        """Test case for kubernetes_node_actions

        Node actions
        """
        pass

    def test_kubernetes_node_list(self) -> None:
        """Test case for kubernetes_node_list

        Retrieve a list of k8s node
        """
        pass

    def test_kubernetes_overview(self) -> None:
        """Test case for kubernetes_overview

        Overview kubernetes nodes and pods by organization id
        """
        pass

    def test_kubernetes_patch_resource(self) -> None:
        """Test case for kubernetes_patch_resource

        Patch kubernetes resource
        """
        pass

    def test_kubernetes_pdb_list(self) -> None:
        """Test case for kubernetes_pdb_list

        Retrieve a list of k8s pdb for all namespaces
        """
        pass

    def test_kubernetes_pod_list(self) -> None:
        """Test case for kubernetes_pod_list

        Retrieve a list of k8s pod for all namespaces
        """
        pass

    def test_kubernetes_pod_logs(self) -> None:
        """Test case for kubernetes_pod_logs

        Retrieve k8s pod logs
        """
        pass

    def test_kubernetes_pvc_list(self) -> None:
        """Test case for kubernetes_pvc_list

        Retrieve a list of k8s pvc for all namespaces
        """
        pass

    def test_kubernetes_quota(self) -> None:
        """Test case for kubernetes_quota

        K8s quota usage
        """
        pass

    def test_kubernetes_removealerts(self) -> None:
        """Test case for kubernetes_removealerts

        Remove k8s alerts
        """
        pass

    def test_kubernetes_resources(self) -> None:
        """Test case for kubernetes_resources

        Retrieve all total count
        """
        pass

    def test_kubernetes_restart_daemon_set(self) -> None:
        """Test case for kubernetes_restart_daemon_set

        Restart daemon set
        """
        pass

    def test_kubernetes_restart_deployment(self) -> None:
        """Test case for kubernetes_restart_deployment

        Restart deployment
        """
        pass

    def test_kubernetes_restart_sts(self) -> None:
        """Test case for kubernetes_restart_sts

        Restart stateful set
        """
        pass

    def test_kubernetes_secret_list(self) -> None:
        """Test case for kubernetes_secret_list

        Retrieve a list of k8s secret for all namespaces
        """
        pass

    def test_kubernetes_service_list(self) -> None:
        """Test case for kubernetes_service_list

        Retrieve a list of k8s service for all namespaces
        """
        pass

    def test_kubernetes_silence_manager(self) -> None:
        """Test case for kubernetes_silence_manager

        Silence management for k8s alerts
        """
        pass

    def test_kubernetes_storage_class_list(self) -> None:
        """Test case for kubernetes_storage_class_list

        Retrieve a list of k8s storageclass for all namespaces
        """
        pass

    def test_kubernetes_sts_actions(self) -> None:
        """Test case for kubernetes_sts_actions

        Stateful set actions
        """
        pass

    def test_kubernetes_sts_list(self) -> None:
        """Test case for kubernetes_sts_list

        Retrieve a list of k8s sts for all namespaces
        """
        pass

    def test_kubernetes_update_alert(self) -> None:
        """Test case for kubernetes_update_alert

        Update k8s alert
        """
        pass


if __name__ == '__main__':
    unittest.main()
