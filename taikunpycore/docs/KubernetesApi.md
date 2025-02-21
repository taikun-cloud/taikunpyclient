# taikunpycore.KubernetesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kubernetes_add_k8s_alert**](KubernetesApi.md#kubernetes_add_k8s_alert) | **POST** /api/v1/kubernetes/alert/{projectId} | Add k8s alert
[**kubernetes_add_k8s_events**](KubernetesApi.md#kubernetes_add_k8s_events) | **POST** /api/v1/kubernetes/event/{projectId} | Add k8s event
[**kubernetes_alert_list**](KubernetesApi.md#kubernetes_alert_list) | **GET** /api/v1/kubernetes/{projectId}/alerts | Retrieve a list of alerts for project
[**kubernetes_cli**](KubernetesApi.md#kubernetes_cli) | **POST** /api/v1/kubernetes/cli | Execute k8s web socket namespaced pod
[**kubernetes_config_map_list**](KubernetesApi.md#kubernetes_config_map_list) | **GET** /api/v1/kubernetes/{projectId}/configmap | Retrieve a list of k8s config map for all namespaces
[**kubernetes_crd_list**](KubernetesApi.md#kubernetes_crd_list) | **GET** /api/v1/kubernetes/{projectId}/crd | Retrieve a list of crd
[**kubernetes_create_resource**](KubernetesApi.md#kubernetes_create_resource) | **POST** /api/v1/kubernetes/create-resource | Create kubernetes resource
[**kubernetes_cron_job_list**](KubernetesApi.md#kubernetes_cron_job_list) | **GET** /api/v1/kubernetes/{projectId}/cronjobs | Retrieve a list of k8s cron jobs for all namespaces
[**kubernetes_cronjob_actions**](KubernetesApi.md#kubernetes_cronjob_actions) | **POST** /api/v1/kubernetes/cronjob/actions | Cronjob actions
[**kubernetes_daemon_set_list**](KubernetesApi.md#kubernetes_daemon_set_list) | **GET** /api/v1/kubernetes/{projectId}/daemonset | Retrieve list of k8s daemonset
[**kubernetes_daemonset_actions**](KubernetesApi.md#kubernetes_daemonset_actions) | **POST** /api/v1/kubernetes/daemonset/actions | Daemonset actions
[**kubernetes_dashboard_list**](KubernetesApi.md#kubernetes_dashboard_list) | **GET** /api/v1/kubernetes/{projectId}/dashboard | Retrieve a list of crd
[**kubernetes_delete_resource**](KubernetesApi.md#kubernetes_delete_resource) | **POST** /api/v1/kubernetes/delete-resource | Delete kubernetes resource
[**kubernetes_deployment_actions**](KubernetesApi.md#kubernetes_deployment_actions) | **POST** /api/v1/kubernetes/deployment/actions | Deployment actions
[**kubernetes_deployment_list**](KubernetesApi.md#kubernetes_deployment_list) | **GET** /api/v1/kubernetes/{projectId}/deployment | Retrieve a list of k8s deployment for all namespaces
[**kubernetes_describe_config_map**](KubernetesApi.md#kubernetes_describe_config_map) | **POST** /api/v1/kubernetes/describe/configmap | Describe configmap
[**kubernetes_describe_crd**](KubernetesApi.md#kubernetes_describe_crd) | **POST** /api/v1/kubernetes/describe/crd | Describe crd
[**kubernetes_describe_cronjob**](KubernetesApi.md#kubernetes_describe_cronjob) | **POST** /api/v1/kubernetes/describe/cronjob | Describe cronjob
[**kubernetes_describe_daemon_set**](KubernetesApi.md#kubernetes_describe_daemon_set) | **POST** /api/v1/kubernetes/describe/daemonset | Describe daemonset
[**kubernetes_describe_deployment**](KubernetesApi.md#kubernetes_describe_deployment) | **POST** /api/v1/kubernetes/describe/deployment | Describe deployment
[**kubernetes_describe_ingress**](KubernetesApi.md#kubernetes_describe_ingress) | **POST** /api/v1/kubernetes/describe/ingress | Describe ingress
[**kubernetes_describe_job**](KubernetesApi.md#kubernetes_describe_job) | **POST** /api/v1/kubernetes/describe/job | Describe job
[**kubernetes_describe_network_policy**](KubernetesApi.md#kubernetes_describe_network_policy) | **POST** /api/v1/kubernetes/describe/network-policy | Describe network policy
[**kubernetes_describe_node**](KubernetesApi.md#kubernetes_describe_node) | **POST** /api/v1/kubernetes/describe/node | Describe node
[**kubernetes_describe_pdb**](KubernetesApi.md#kubernetes_describe_pdb) | **POST** /api/v1/kubernetes/describe/pdb | Describe pdb
[**kubernetes_describe_pod**](KubernetesApi.md#kubernetes_describe_pod) | **POST** /api/v1/kubernetes/describe/pod | Describe pod
[**kubernetes_describe_pvc**](KubernetesApi.md#kubernetes_describe_pvc) | **POST** /api/v1/kubernetes/describe/pvc | Describe pvc
[**kubernetes_describe_resource**](KubernetesApi.md#kubernetes_describe_resource) | **POST** /api/v1/kubernetes/describe-resource | Describe kubernetes resource
[**kubernetes_describe_secret**](KubernetesApi.md#kubernetes_describe_secret) | **POST** /api/v1/kubernetes/describe/secret | Describe secret
[**kubernetes_describe_service**](KubernetesApi.md#kubernetes_describe_service) | **POST** /api/v1/kubernetes/describe/service | Describe service
[**kubernetes_describe_storage_class**](KubernetesApi.md#kubernetes_describe_storage_class) | **POST** /api/v1/kubernetes/describe/storageclass | Describe storage class
[**kubernetes_describe_sts**](KubernetesApi.md#kubernetes_describe_sts) | **POST** /api/v1/kubernetes/describe/sts | Describe stateful set
[**kubernetes_download**](KubernetesApi.md#kubernetes_download) | **GET** /api/v1/kubernetes/{projectId}/download | Download kube config file
[**kubernetes_download_manifest**](KubernetesApi.md#kubernetes_download_manifest) | **POST** /api/v1/kubernetes/download-manifest | Download manifest
[**kubernetes_export**](KubernetesApi.md#kubernetes_export) | **GET** /api/v1/kubernetes/export | Export
[**kubernetes_forbidden_namespaces**](KubernetesApi.md#kubernetes_forbidden_namespaces) | **GET** /api/v1/kubernetes/forbidden-namespaces/{projectId} | Forbidden namespaces for k8s actions
[**kubernetes_get_supported_list**](KubernetesApi.md#kubernetes_get_supported_list) | **GET** /api/v1/kubernetes/supported/list | Retrieve Taikun supported kubernetes versions
[**kubernetes_helm_release_list**](KubernetesApi.md#kubernetes_helm_release_list) | **GET** /api/v1/kubernetes/{projectId}/helmreleases | Retrieve a list of k8s helm releases for all namespaces
[**kubernetes_ingress_classes**](KubernetesApi.md#kubernetes_ingress_classes) | **POST** /api/v1/kubernetes/ingress-classes | List of ingress classes
[**kubernetes_ingress_list**](KubernetesApi.md#kubernetes_ingress_list) | **GET** /api/v1/kubernetes/{projectId}/ingress | Retrieve a list of k8s ingress for all namespaces
[**kubernetes_interactive_shell**](KubernetesApi.md#kubernetes_interactive_shell) | **POST** /api/v1/kubernetes/interactive-shell | Produce interactive shell command
[**kubernetes_jobs_list**](KubernetesApi.md#kubernetes_jobs_list) | **GET** /api/v1/kubernetes/{projectId}/jobs | Retrieve a list of k8s jobs for all namespaces
[**kubernetes_kill_pod**](KubernetesApi.md#kubernetes_kill_pod) | **POST** /api/v1/kubernetes/{projectId}/deletepod/{metadataName}/{namespace} | Kill the pod
[**kubernetes_kube_config**](KubernetesApi.md#kubernetes_kube_config) | **GET** /api/v1/kubernetes/{projectId}/kubeconfig | Retrieve kube config file
[**kubernetes_namespace_list**](KubernetesApi.md#kubernetes_namespace_list) | **GET** /api/v1/kubernetes/{projectId}/namespaces | Retrieve kube config file
[**kubernetes_network_policy_list**](KubernetesApi.md#kubernetes_network_policy_list) | **GET** /api/v1/kubernetes/{projectId}/network-policies | Retrieve a list of k8s network-policies for all namespaces
[**kubernetes_node_actions**](KubernetesApi.md#kubernetes_node_actions) | **POST** /api/v1/kubernetes/nodes/actions | Node actions
[**kubernetes_node_list**](KubernetesApi.md#kubernetes_node_list) | **GET** /api/v1/kubernetes/{projectId}/node | Retrieve a list of k8s node
[**kubernetes_overview**](KubernetesApi.md#kubernetes_overview) | **GET** /api/v1/kubernetes/overview | Overview kubernetes nodes and pods by organization id
[**kubernetes_patch_resource**](KubernetesApi.md#kubernetes_patch_resource) | **POST** /api/v1/kubernetes/patch-resource | Patch kubernetes resource
[**kubernetes_pdb_list**](KubernetesApi.md#kubernetes_pdb_list) | **GET** /api/v1/kubernetes/{projectId}/pdb | Retrieve a list of k8s pdb for all namespaces
[**kubernetes_pod_list**](KubernetesApi.md#kubernetes_pod_list) | **GET** /api/v1/kubernetes/{projectId}/pod | Retrieve a list of k8s pod for all namespaces
[**kubernetes_pod_logs**](KubernetesApi.md#kubernetes_pod_logs) | **POST** /api/v1/kubernetes/podLogs | Retrieve k8s pod logs
[**kubernetes_pvc_list**](KubernetesApi.md#kubernetes_pvc_list) | **GET** /api/v1/kubernetes/{projectId}/pvc | Retrieve a list of k8s pvc for all namespaces
[**kubernetes_quota**](KubernetesApi.md#kubernetes_quota) | **GET** /api/v1/kubernetes/{projectId}/quota | K8s quota usage
[**kubernetes_removealerts**](KubernetesApi.md#kubernetes_removealerts) | **POST** /api/v1/kubernetes/removealerts | Remove k8s alerts
[**kubernetes_resources**](KubernetesApi.md#kubernetes_resources) | **GET** /api/v1/kubernetes/{projectId}/resources | Retrieve all total count
[**kubernetes_restart_daemon_set**](KubernetesApi.md#kubernetes_restart_daemon_set) | **POST** /api/v1/kubernetes/restart/daemonset | Restart daemon set
[**kubernetes_restart_deployment**](KubernetesApi.md#kubernetes_restart_deployment) | **POST** /api/v1/kubernetes/restart/deployment | Restart deployment
[**kubernetes_restart_sts**](KubernetesApi.md#kubernetes_restart_sts) | **POST** /api/v1/kubernetes/restart/sts | Restart stateful set
[**kubernetes_secret_list**](KubernetesApi.md#kubernetes_secret_list) | **GET** /api/v1/kubernetes/{projectId}/secret | Retrieve a list of k8s secret for all namespaces
[**kubernetes_service_list**](KubernetesApi.md#kubernetes_service_list) | **GET** /api/v1/kubernetes/{projectId}/service | Retrieve a list of k8s service for all namespaces
[**kubernetes_silence_manager**](KubernetesApi.md#kubernetes_silence_manager) | **POST** /api/v1/kubernetes/silencemanager | Silence management for k8s alerts
[**kubernetes_storage_class_list**](KubernetesApi.md#kubernetes_storage_class_list) | **GET** /api/v1/kubernetes/{projectId}/storageclass | Retrieve a list of k8s storageclass for all namespaces
[**kubernetes_sts_actions**](KubernetesApi.md#kubernetes_sts_actions) | **POST** /api/v1/kubernetes/sts/actions | Stateful set actions
[**kubernetes_sts_list**](KubernetesApi.md#kubernetes_sts_list) | **GET** /api/v1/kubernetes/{projectId}/sts | Retrieve a list of k8s sts for all namespaces
[**kubernetes_update_alert**](KubernetesApi.md#kubernetes_update_alert) | **PUT** /api/v1/kubernetes/updatealert/{alertId} | Update k8s alert


# **kubernetes_add_k8s_alert**
> object kubernetes_add_k8s_alert(project_id, create_alert_dto=create_alert_dto)

Add k8s alert

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_alert_dto import CreateAlertDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    create_alert_dto = taikunpycore.CreateAlertDto() # CreateAlertDto |  (optional)

    try:
        # Add k8s alert
        api_response = api_instance.kubernetes_add_k8s_alert(project_id, create_alert_dto=create_alert_dto)
        print("The response of KubernetesApi->kubernetes_add_k8s_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_add_k8s_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **create_alert_dto** | [**CreateAlertDto**](CreateAlertDto.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_add_k8s_events**
> object kubernetes_add_k8s_events(project_id, kubernetes_event_create_dto=kubernetes_event_create_dto)

Add k8s event

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_event_create_dto import KubernetesEventCreateDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    kubernetes_event_create_dto = taikunpycore.KubernetesEventCreateDto() # KubernetesEventCreateDto |  (optional)

    try:
        # Add k8s event
        api_response = api_instance.kubernetes_add_k8s_events(project_id, kubernetes_event_create_dto=kubernetes_event_create_dto)
        print("The response of KubernetesApi->kubernetes_add_k8s_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_add_k8s_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **kubernetes_event_create_dto** | [**KubernetesEventCreateDto**](KubernetesEventCreateDto.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_alert_list**
> KubernetesAlertList kubernetes_alert_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, type=type, start_date=start_date, end_date=end_date)

Retrieve a list of alerts for project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_alert_list import KubernetesAlertList
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Retrieve a list of alerts for project
        api_response = api_instance.kubernetes_alert_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, type=type, start_date=start_date, end_date=end_date)
        print("The response of KubernetesApi->kubernetes_alert_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_alert_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**KubernetesAlertList**](KubernetesAlertList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_cli**
> str kubernetes_cli(kubernetes_cli_command)

Execute k8s web socket namespaced pod

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_cli_command import KubernetesCliCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    kubernetes_cli_command = taikunpycore.KubernetesCliCommand() # KubernetesCliCommand | 

    try:
        # Execute k8s web socket namespaced pod
        api_response = api_instance.kubernetes_cli(kubernetes_cli_command)
        print("The response of KubernetesApi->kubernetes_cli:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_cli: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_cli_command** | [**KubernetesCliCommand**](KubernetesCliCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_config_map_list**
> ConfigMaps kubernetes_config_map_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s config map for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.config_maps import ConfigMaps
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s config map for all namespaces
        api_response = api_instance.kubernetes_config_map_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_config_map_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_config_map_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**ConfigMaps**](ConfigMaps.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_crd_list**
> Crds kubernetes_crd_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of crd

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.crds import Crds
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of crd
        api_response = api_instance.kubernetes_crd_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_crd_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_crd_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Crds**](Crds.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_create_resource**
> object kubernetes_create_resource(create_kubernetes_resource_command=create_kubernetes_resource_command)

Create kubernetes resource

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_kubernetes_resource_command import CreateKubernetesResourceCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    create_kubernetes_resource_command = taikunpycore.CreateKubernetesResourceCommand() # CreateKubernetesResourceCommand |  (optional)

    try:
        # Create kubernetes resource
        api_response = api_instance.kubernetes_create_resource(create_kubernetes_resource_command=create_kubernetes_resource_command)
        print("The response of KubernetesApi->kubernetes_create_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_create_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_kubernetes_resource_command** | [**CreateKubernetesResourceCommand**](CreateKubernetesResourceCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_cron_job_list**
> KubernetesCronJobsList kubernetes_cron_job_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s cron jobs for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_cron_jobs_list import KubernetesCronJobsList
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s cron jobs for all namespaces
        api_response = api_instance.kubernetes_cron_job_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_cron_job_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_cron_job_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**KubernetesCronJobsList**](KubernetesCronJobsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_cronjob_actions**
> object kubernetes_cronjob_actions(cronjob_action_command=cronjob_action_command)

Cronjob actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cronjob_action_command import CronjobActionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    cronjob_action_command = taikunpycore.CronjobActionCommand() # CronjobActionCommand |  (optional)

    try:
        # Cronjob actions
        api_response = api_instance.kubernetes_cronjob_actions(cronjob_action_command=cronjob_action_command)
        print("The response of KubernetesApi->kubernetes_cronjob_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_cronjob_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cronjob_action_command** | [**CronjobActionCommand**](CronjobActionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_daemon_set_list**
> DaemonSets kubernetes_daemon_set_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve list of k8s daemonset

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.daemon_sets import DaemonSets
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve list of k8s daemonset
        api_response = api_instance.kubernetes_daemon_set_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_daemon_set_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_daemon_set_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**DaemonSets**](DaemonSets.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_daemonset_actions**
> object kubernetes_daemonset_actions(daemonset_action_command=daemonset_action_command)

Daemonset actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.daemonset_action_command import DaemonsetActionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    daemonset_action_command = taikunpycore.DaemonsetActionCommand() # DaemonsetActionCommand |  (optional)

    try:
        # Daemonset actions
        api_response = api_instance.kubernetes_daemonset_actions(daemonset_action_command=daemonset_action_command)
        print("The response of KubernetesApi->kubernetes_daemonset_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_daemonset_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **daemonset_action_command** | [**DaemonsetActionCommand**](DaemonsetActionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_dashboard_list**
> KubernetesDashboardDto kubernetes_dashboard_list(project_id)

Retrieve a list of crd

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_dashboard_dto import KubernetesDashboardDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # Retrieve a list of crd
        api_response = api_instance.kubernetes_dashboard_list(project_id)
        print("The response of KubernetesApi->kubernetes_dashboard_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_dashboard_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**KubernetesDashboardDto**](KubernetesDashboardDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_delete_resource**
> KubernetesActionResponse kubernetes_delete_resource(delete_kubernetes_resource_command=delete_kubernetes_resource_command)

Delete kubernetes resource

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_kubernetes_resource_command import DeleteKubernetesResourceCommand
from taikunpycore.models.kubernetes_action_response import KubernetesActionResponse
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    delete_kubernetes_resource_command = taikunpycore.DeleteKubernetesResourceCommand() # DeleteKubernetesResourceCommand |  (optional)

    try:
        # Delete kubernetes resource
        api_response = api_instance.kubernetes_delete_resource(delete_kubernetes_resource_command=delete_kubernetes_resource_command)
        print("The response of KubernetesApi->kubernetes_delete_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_delete_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_kubernetes_resource_command** | [**DeleteKubernetesResourceCommand**](DeleteKubernetesResourceCommand.md)|  | [optional] 

### Return type

[**KubernetesActionResponse**](KubernetesActionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_deployment_actions**
> object kubernetes_deployment_actions(deployment_action_command=deployment_action_command)

Deployment actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_action_command import DeploymentActionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    deployment_action_command = taikunpycore.DeploymentActionCommand() # DeploymentActionCommand |  (optional)

    try:
        # Deployment actions
        api_response = api_instance.kubernetes_deployment_actions(deployment_action_command=deployment_action_command)
        print("The response of KubernetesApi->kubernetes_deployment_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_deployment_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_action_command** | [**DeploymentActionCommand**](DeploymentActionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_deployment_list**
> Deployments kubernetes_deployment_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s deployment for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployments import Deployments
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s deployment for all namespaces
        api_response = api_instance.kubernetes_deployment_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_deployment_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_deployment_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Deployments**](Deployments.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_config_map**
> str kubernetes_describe_config_map(describe_config_map_command)

Describe configmap

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_config_map_command import DescribeConfigMapCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_config_map_command = taikunpycore.DescribeConfigMapCommand() # DescribeConfigMapCommand | 

    try:
        # Describe configmap
        api_response = api_instance.kubernetes_describe_config_map(describe_config_map_command)
        print("The response of KubernetesApi->kubernetes_describe_config_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_config_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_config_map_command** | [**DescribeConfigMapCommand**](DescribeConfigMapCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_crd**
> str kubernetes_describe_crd(describe_crd_command)

Describe crd

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_crd_command import DescribeCrdCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_crd_command = taikunpycore.DescribeCrdCommand() # DescribeCrdCommand | 

    try:
        # Describe crd
        api_response = api_instance.kubernetes_describe_crd(describe_crd_command)
        print("The response of KubernetesApi->kubernetes_describe_crd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_crd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_crd_command** | [**DescribeCrdCommand**](DescribeCrdCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_cronjob**
> str kubernetes_describe_cronjob(describe_cron_job_command)

Describe cronjob

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_cron_job_command import DescribeCronJobCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_cron_job_command = taikunpycore.DescribeCronJobCommand() # DescribeCronJobCommand | 

    try:
        # Describe cronjob
        api_response = api_instance.kubernetes_describe_cronjob(describe_cron_job_command)
        print("The response of KubernetesApi->kubernetes_describe_cronjob:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_cronjob: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_cron_job_command** | [**DescribeCronJobCommand**](DescribeCronJobCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_daemon_set**
> str kubernetes_describe_daemon_set(describe_daemon_set_command)

Describe daemonset

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_daemon_set_command import DescribeDaemonSetCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_daemon_set_command = taikunpycore.DescribeDaemonSetCommand() # DescribeDaemonSetCommand | 

    try:
        # Describe daemonset
        api_response = api_instance.kubernetes_describe_daemon_set(describe_daemon_set_command)
        print("The response of KubernetesApi->kubernetes_describe_daemon_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_daemon_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_daemon_set_command** | [**DescribeDaemonSetCommand**](DescribeDaemonSetCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_deployment**
> str kubernetes_describe_deployment(describe_deployment_command)

Describe deployment

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_deployment_command import DescribeDeploymentCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_deployment_command = taikunpycore.DescribeDeploymentCommand() # DescribeDeploymentCommand | 

    try:
        # Describe deployment
        api_response = api_instance.kubernetes_describe_deployment(describe_deployment_command)
        print("The response of KubernetesApi->kubernetes_describe_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_deployment_command** | [**DescribeDeploymentCommand**](DescribeDeploymentCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_ingress**
> str kubernetes_describe_ingress(describe_ingress_command)

Describe ingress

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_ingress_command import DescribeIngressCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_ingress_command = taikunpycore.DescribeIngressCommand() # DescribeIngressCommand | 

    try:
        # Describe ingress
        api_response = api_instance.kubernetes_describe_ingress(describe_ingress_command)
        print("The response of KubernetesApi->kubernetes_describe_ingress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_ingress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_ingress_command** | [**DescribeIngressCommand**](DescribeIngressCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_job**
> str kubernetes_describe_job(describe_job_command)

Describe job

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_job_command import DescribeJobCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_job_command = taikunpycore.DescribeJobCommand() # DescribeJobCommand | 

    try:
        # Describe job
        api_response = api_instance.kubernetes_describe_job(describe_job_command)
        print("The response of KubernetesApi->kubernetes_describe_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_job_command** | [**DescribeJobCommand**](DescribeJobCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_network_policy**
> str kubernetes_describe_network_policy(describe_network_policy_command)

Describe network policy

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_network_policy_command import DescribeNetworkPolicyCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_network_policy_command = taikunpycore.DescribeNetworkPolicyCommand() # DescribeNetworkPolicyCommand | 

    try:
        # Describe network policy
        api_response = api_instance.kubernetes_describe_network_policy(describe_network_policy_command)
        print("The response of KubernetesApi->kubernetes_describe_network_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_network_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_network_policy_command** | [**DescribeNetworkPolicyCommand**](DescribeNetworkPolicyCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_node**
> str kubernetes_describe_node(describe_node_command)

Describe node

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_node_command import DescribeNodeCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_node_command = taikunpycore.DescribeNodeCommand() # DescribeNodeCommand | 

    try:
        # Describe node
        api_response = api_instance.kubernetes_describe_node(describe_node_command)
        print("The response of KubernetesApi->kubernetes_describe_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_node_command** | [**DescribeNodeCommand**](DescribeNodeCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_pdb**
> str kubernetes_describe_pdb(describe_pod_disruption_command)

Describe pdb

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_pod_disruption_command import DescribePodDisruptionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_pod_disruption_command = taikunpycore.DescribePodDisruptionCommand() # DescribePodDisruptionCommand | 

    try:
        # Describe pdb
        api_response = api_instance.kubernetes_describe_pdb(describe_pod_disruption_command)
        print("The response of KubernetesApi->kubernetes_describe_pdb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_pdb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_pod_disruption_command** | [**DescribePodDisruptionCommand**](DescribePodDisruptionCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_pod**
> str kubernetes_describe_pod(describe_pod_command)

Describe pod

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_pod_command import DescribePodCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_pod_command = taikunpycore.DescribePodCommand() # DescribePodCommand | 

    try:
        # Describe pod
        api_response = api_instance.kubernetes_describe_pod(describe_pod_command)
        print("The response of KubernetesApi->kubernetes_describe_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_pod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_pod_command** | [**DescribePodCommand**](DescribePodCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_pvc**
> str kubernetes_describe_pvc(describe_pvc_command)

Describe pvc

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_pvc_command import DescribePvcCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_pvc_command = taikunpycore.DescribePvcCommand() # DescribePvcCommand | 

    try:
        # Describe pvc
        api_response = api_instance.kubernetes_describe_pvc(describe_pvc_command)
        print("The response of KubernetesApi->kubernetes_describe_pvc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_pvc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_pvc_command** | [**DescribePvcCommand**](DescribePvcCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_resource**
> str kubernetes_describe_resource(describe_kubernetes_resource_command=describe_kubernetes_resource_command)

Describe kubernetes resource

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_kubernetes_resource_command import DescribeKubernetesResourceCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_kubernetes_resource_command = taikunpycore.DescribeKubernetesResourceCommand() # DescribeKubernetesResourceCommand |  (optional)

    try:
        # Describe kubernetes resource
        api_response = api_instance.kubernetes_describe_resource(describe_kubernetes_resource_command=describe_kubernetes_resource_command)
        print("The response of KubernetesApi->kubernetes_describe_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_kubernetes_resource_command** | [**DescribeKubernetesResourceCommand**](DescribeKubernetesResourceCommand.md)|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_secret**
> str kubernetes_describe_secret(describe_secret_command)

Describe secret

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_secret_command import DescribeSecretCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_secret_command = taikunpycore.DescribeSecretCommand() # DescribeSecretCommand | 

    try:
        # Describe secret
        api_response = api_instance.kubernetes_describe_secret(describe_secret_command)
        print("The response of KubernetesApi->kubernetes_describe_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_secret_command** | [**DescribeSecretCommand**](DescribeSecretCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_service**
> str kubernetes_describe_service(describe_service_command)

Describe service

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_service_command import DescribeServiceCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_service_command = taikunpycore.DescribeServiceCommand() # DescribeServiceCommand | 

    try:
        # Describe service
        api_response = api_instance.kubernetes_describe_service(describe_service_command)
        print("The response of KubernetesApi->kubernetes_describe_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_service_command** | [**DescribeServiceCommand**](DescribeServiceCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_storage_class**
> str kubernetes_describe_storage_class(describe_storage_class_command)

Describe storage class

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_storage_class_command import DescribeStorageClassCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_storage_class_command = taikunpycore.DescribeStorageClassCommand() # DescribeStorageClassCommand | 

    try:
        # Describe storage class
        api_response = api_instance.kubernetes_describe_storage_class(describe_storage_class_command)
        print("The response of KubernetesApi->kubernetes_describe_storage_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_storage_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_storage_class_command** | [**DescribeStorageClassCommand**](DescribeStorageClassCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_describe_sts**
> str kubernetes_describe_sts(describe_sts_command)

Describe stateful set

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.describe_sts_command import DescribeStsCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    describe_sts_command = taikunpycore.DescribeStsCommand() # DescribeStsCommand | 

    try:
        # Describe stateful set
        api_response = api_instance.kubernetes_describe_sts(describe_sts_command)
        print("The response of KubernetesApi->kubernetes_describe_sts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_describe_sts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_sts_command** | [**DescribeStsCommand**](DescribeStsCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_download**
> object kubernetes_download(project_id)

Download kube config file

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # Download kube config file
        api_response = api_instance.kubernetes_download(project_id)
        print("The response of KubernetesApi->kubernetes_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_download_manifest**
> CsvExporter kubernetes_download_manifest(download_kubernetes_resource_command=download_kubernetes_resource_command)

Download manifest

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.csv_exporter import CsvExporter
from taikunpycore.models.download_kubernetes_resource_command import DownloadKubernetesResourceCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    download_kubernetes_resource_command = taikunpycore.DownloadKubernetesResourceCommand() # DownloadKubernetesResourceCommand |  (optional)

    try:
        # Download manifest
        api_response = api_instance.kubernetes_download_manifest(download_kubernetes_resource_command=download_kubernetes_resource_command)
        print("The response of KubernetesApi->kubernetes_download_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_download_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_kubernetes_resource_command** | [**DownloadKubernetesResourceCommand**](DownloadKubernetesResourceCommand.md)|  | [optional] 

### Return type

[**CsvExporter**](CsvExporter.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_export**
> CsvExporter kubernetes_export(project_id)

Export

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.csv_exporter import CsvExporter
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # Export
        api_response = api_instance.kubernetes_export(project_id)
        print("The response of KubernetesApi->kubernetes_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**CsvExporter**](CsvExporter.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_forbidden_namespaces**
> List[str] kubernetes_forbidden_namespaces(project_id)

Forbidden namespaces for k8s actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # Forbidden namespaces for k8s actions
        api_response = api_instance.kubernetes_forbidden_namespaces(project_id)
        print("The response of KubernetesApi->kubernetes_forbidden_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_forbidden_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

**List[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_get_supported_list**
> List[KubernetesVersionListDto] kubernetes_get_supported_list()

Retrieve Taikun supported kubernetes versions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_version_list_dto import KubernetesVersionListDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)

    try:
        # Retrieve Taikun supported kubernetes versions
        api_response = api_instance.kubernetes_get_supported_list()
        print("The response of KubernetesApi->kubernetes_get_supported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_get_supported_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[KubernetesVersionListDto]**](KubernetesVersionListDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_helm_release_list**
> HelmReleasesList kubernetes_helm_release_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s helm releases for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.helm_releases_list import HelmReleasesList
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s helm releases for all namespaces
        api_response = api_instance.kubernetes_helm_release_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_helm_release_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_helm_release_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**HelmReleasesList**](HelmReleasesList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_ingress_classes**
> List[str] kubernetes_ingress_classes(config=config, cloud_id=cloud_id, region=region, import_cluster_name=import_cluster_name, resource_group_name=resource_group_name)

List of ingress classes

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    config = None # bytearray |  (optional)
    cloud_id = 56 # int |  (optional)
    region = 'region_example' # str |  (optional)
    import_cluster_name = 'import_cluster_name_example' # str |  (optional)
    resource_group_name = 'resource_group_name_example' # str |  (optional)

    try:
        # List of ingress classes
        api_response = api_instance.kubernetes_ingress_classes(config=config, cloud_id=cloud_id, region=region, import_cluster_name=import_cluster_name, resource_group_name=resource_group_name)
        print("The response of KubernetesApi->kubernetes_ingress_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_ingress_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **bytearray**|  | [optional] 
 **cloud_id** | **int**|  | [optional] 
 **region** | **str**|  | [optional] 
 **import_cluster_name** | **str**|  | [optional] 
 **resource_group_name** | **str**|  | [optional] 

### Return type

**List[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_ingress_list**
> Ingresses kubernetes_ingress_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s ingress for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ingresses import Ingresses
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s ingress for all namespaces
        api_response = api_instance.kubernetes_ingress_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_ingress_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_ingress_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Ingresses**](Ingresses.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_interactive_shell**
> KubernetesInteractiveShellDto kubernetes_interactive_shell(interactive_shell_send_command)

Produce interactive shell command

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.interactive_shell_send_command import InteractiveShellSendCommand
from taikunpycore.models.kubernetes_interactive_shell_dto import KubernetesInteractiveShellDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    interactive_shell_send_command = taikunpycore.InteractiveShellSendCommand() # InteractiveShellSendCommand | 

    try:
        # Produce interactive shell command
        api_response = api_instance.kubernetes_interactive_shell(interactive_shell_send_command)
        print("The response of KubernetesApi->kubernetes_interactive_shell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_interactive_shell: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interactive_shell_send_command** | [**InteractiveShellSendCommand**](InteractiveShellSendCommand.md)|  | 

### Return type

[**KubernetesInteractiveShellDto**](KubernetesInteractiveShellDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_jobs_list**
> KubernetesJobList kubernetes_jobs_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s jobs for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_job_list import KubernetesJobList
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s jobs for all namespaces
        api_response = api_instance.kubernetes_jobs_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_jobs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_jobs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**KubernetesJobList**](KubernetesJobList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_kill_pod**
> object kubernetes_kill_pod(project_id, metadata_name, namespace)

Kill the pod

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    metadata_name = 'metadata_name_example' # str | 
    namespace = 'namespace_example' # str | 

    try:
        # Kill the pod
        api_response = api_instance.kubernetes_kill_pod(project_id, metadata_name, namespace)
        print("The response of KubernetesApi->kubernetes_kill_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_kill_pod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **metadata_name** | **str**|  | 
 **namespace** | **str**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_kube_config**
> KubeConfigResponse kubernetes_kube_config(project_id)

Retrieve kube config file

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kube_config_response import KubeConfigResponse
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # Retrieve kube config file
        api_response = api_instance.kubernetes_kube_config(project_id)
        print("The response of KubernetesApi->kubernetes_kube_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_kube_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**KubeConfigResponse**](KubeConfigResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_namespace_list**
> List[str] kubernetes_namespace_list(project_id, installation=installation)

Retrieve kube config file

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    installation = True # bool |  (optional)

    try:
        # Retrieve kube config file
        api_response = api_instance.kubernetes_namespace_list(project_id, installation=installation)
        print("The response of KubernetesApi->kubernetes_namespace_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_namespace_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **installation** | **bool**|  | [optional] 

### Return type

**List[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_network_policy_list**
> NetworkPolicies kubernetes_network_policy_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s network-policies for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.network_policies import NetworkPolicies
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s network-policies for all namespaces
        api_response = api_instance.kubernetes_network_policy_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_network_policy_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_network_policy_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**NetworkPolicies**](NetworkPolicies.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_node_actions**
> object kubernetes_node_actions(node_action_command=node_action_command)

Node actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.node_action_command import NodeActionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    node_action_command = taikunpycore.NodeActionCommand() # NodeActionCommand |  (optional)

    try:
        # Node actions
        api_response = api_instance.kubernetes_node_actions(node_action_command=node_action_command)
        print("The response of KubernetesApi->kubernetes_node_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_node_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_action_command** | [**NodeActionCommand**](NodeActionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_node_list**
> List[KubernetesNodeListDto] kubernetes_node_list(project_id, search_id=search_id)

Retrieve a list of k8s node

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_node_list_dto import KubernetesNodeListDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    search_id = 'search_id_example' # str |  (optional)

    try:
        # Retrieve a list of k8s node
        api_response = api_instance.kubernetes_node_list(project_id, search_id=search_id)
        print("The response of KubernetesApi->kubernetes_node_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_node_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **search_id** | **str**|  | [optional] 

### Return type

[**List[KubernetesNodeListDto]**](KubernetesNodeListDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_overview**
> List[KubernetesOverviewDto] kubernetes_overview(organization_id=organization_id)

Overview kubernetes nodes and pods by organization id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_overview_dto import KubernetesOverviewDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Overview kubernetes nodes and pods by organization id
        api_response = api_instance.kubernetes_overview(organization_id=organization_id)
        print("The response of KubernetesApi->kubernetes_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

[**List[KubernetesOverviewDto]**](KubernetesOverviewDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_patch_resource**
> object kubernetes_patch_resource(patch_kubernetes_resource_command=patch_kubernetes_resource_command)

Patch kubernetes resource

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.patch_kubernetes_resource_command import PatchKubernetesResourceCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    patch_kubernetes_resource_command = taikunpycore.PatchKubernetesResourceCommand() # PatchKubernetesResourceCommand |  (optional)

    try:
        # Patch kubernetes resource
        api_response = api_instance.kubernetes_patch_resource(patch_kubernetes_resource_command=patch_kubernetes_resource_command)
        print("The response of KubernetesApi->kubernetes_patch_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_patch_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_kubernetes_resource_command** | [**PatchKubernetesResourceCommand**](PatchKubernetesResourceCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_pdb_list**
> PodDisruptions kubernetes_pdb_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s pdb for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.pod_disruptions import PodDisruptions
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s pdb for all namespaces
        api_response = api_instance.kubernetes_pdb_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_pdb_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_pdb_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**PodDisruptions**](PodDisruptions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_pod_list**
> Pods kubernetes_pod_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s pod for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.pods import Pods
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s pod for all namespaces
        api_response = api_instance.kubernetes_pod_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_pod_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_pod_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Pods**](Pods.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_pod_logs**
> str kubernetes_pod_logs(kubernetes_pod_logs_command)

Retrieve k8s pod logs

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_pod_logs_command import KubernetesPodLogsCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    kubernetes_pod_logs_command = taikunpycore.KubernetesPodLogsCommand() # KubernetesPodLogsCommand | 

    try:
        # Retrieve k8s pod logs
        api_response = api_instance.kubernetes_pod_logs(kubernetes_pod_logs_command)
        print("The response of KubernetesApi->kubernetes_pod_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_pod_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_pod_logs_command** | [**KubernetesPodLogsCommand**](KubernetesPodLogsCommand.md)|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_pvc_list**
> Pvcs kubernetes_pvc_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s pvc for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.pvcs import Pvcs
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s pvc for all namespaces
        api_response = api_instance.kubernetes_pvc_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_pvc_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_pvc_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Pvcs**](Pvcs.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_quota**
> KubernetesQuotaListDto kubernetes_quota(project_id)

K8s quota usage

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_quota_list_dto import KubernetesQuotaListDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # K8s quota usage
        api_response = api_instance.kubernetes_quota(project_id)
        print("The response of KubernetesApi->kubernetes_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**KubernetesQuotaListDto**](KubernetesQuotaListDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_removealerts**
> object kubernetes_removealerts(delete_alert_command)

Remove k8s alerts

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_alert_command import DeleteAlertCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    delete_alert_command = taikunpycore.DeleteAlertCommand() # DeleteAlertCommand | 

    try:
        # Remove k8s alerts
        api_response = api_instance.kubernetes_removealerts(delete_alert_command)
        print("The response of KubernetesApi->kubernetes_removealerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_removealerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_alert_command** | [**DeleteAlertCommand**](DeleteAlertCommand.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_resources**
> KubernetesResourcesDto kubernetes_resources(project_id)

Retrieve all total count

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_resources_dto import KubernetesResourcesDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 

    try:
        # Retrieve all total count
        api_response = api_instance.kubernetes_resources(project_id)
        print("The response of KubernetesApi->kubernetes_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**KubernetesResourcesDto**](KubernetesResourcesDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_restart_daemon_set**
> object kubernetes_restart_daemon_set(restart_daemon_set_command)

Restart daemon set

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.restart_daemon_set_command import RestartDaemonSetCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    restart_daemon_set_command = taikunpycore.RestartDaemonSetCommand() # RestartDaemonSetCommand | 

    try:
        # Restart daemon set
        api_response = api_instance.kubernetes_restart_daemon_set(restart_daemon_set_command)
        print("The response of KubernetesApi->kubernetes_restart_daemon_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_restart_daemon_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restart_daemon_set_command** | [**RestartDaemonSetCommand**](RestartDaemonSetCommand.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_restart_deployment**
> object kubernetes_restart_deployment(restart_deployment_command)

Restart deployment

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.restart_deployment_command import RestartDeploymentCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    restart_deployment_command = taikunpycore.RestartDeploymentCommand() # RestartDeploymentCommand | 

    try:
        # Restart deployment
        api_response = api_instance.kubernetes_restart_deployment(restart_deployment_command)
        print("The response of KubernetesApi->kubernetes_restart_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_restart_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restart_deployment_command** | [**RestartDeploymentCommand**](RestartDeploymentCommand.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_restart_sts**
> object kubernetes_restart_sts(restart_sts_command)

Restart stateful set

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.restart_sts_command import RestartStsCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    restart_sts_command = taikunpycore.RestartStsCommand() # RestartStsCommand | 

    try:
        # Restart stateful set
        api_response = api_instance.kubernetes_restart_sts(restart_sts_command)
        print("The response of KubernetesApi->kubernetes_restart_sts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_restart_sts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restart_sts_command** | [**RestartStsCommand**](RestartStsCommand.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_secret_list**
> Secrets kubernetes_secret_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s secret for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.secrets import Secrets
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s secret for all namespaces
        api_response = api_instance.kubernetes_secret_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_secret_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_secret_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Secrets**](Secrets.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_service_list**
> Services kubernetes_service_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s service for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.services import Services
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s service for all namespaces
        api_response = api_instance.kubernetes_service_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_service_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_service_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**Services**](Services.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_silence_manager**
> object kubernetes_silence_manager(silence_operations_command)

Silence management for k8s alerts

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.silence_operations_command import SilenceOperationsCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    silence_operations_command = taikunpycore.SilenceOperationsCommand() # SilenceOperationsCommand | 

    try:
        # Silence management for k8s alerts
        api_response = api_instance.kubernetes_silence_manager(silence_operations_command)
        print("The response of KubernetesApi->kubernetes_silence_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_silence_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silence_operations_command** | [**SilenceOperationsCommand**](SilenceOperationsCommand.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_storage_class_list**
> StorageClasses kubernetes_storage_class_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s storageclass for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.storage_classes import StorageClasses
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s storageclass for all namespaces
        api_response = api_instance.kubernetes_storage_class_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_storage_class_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_storage_class_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**StorageClasses**](StorageClasses.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_sts_actions**
> object kubernetes_sts_actions(sts_action_command=sts_action_command)

Stateful set actions

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.sts_action_command import StsActionCommand
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    sts_action_command = taikunpycore.StsActionCommand() # StsActionCommand |  (optional)

    try:
        # Stateful set actions
        api_response = api_instance.kubernetes_sts_actions(sts_action_command=sts_action_command)
        print("The response of KubernetesApi->kubernetes_sts_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_sts_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sts_action_command** | [**StsActionCommand**](StsActionCommand.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_sts_list**
> StsList kubernetes_sts_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)

Retrieve a list of k8s sts for all namespaces

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.sts_list import StsList
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    filter_by = 'filter_by_example' # str |  (optional)

    try:
        # Retrieve a list of k8s sts for all namespaces
        api_response = api_instance.kubernetes_sts_list(project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, filter_by=filter_by)
        print("The response of KubernetesApi->kubernetes_sts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_sts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **filter_by** | **str**|  | [optional] 

### Return type

[**StsList**](StsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_update_alert**
> object kubernetes_update_alert(alert_id, update_kubernetes_alert_dto=update_kubernetes_alert_dto)

Update k8s alert

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_kubernetes_alert_dto import UpdateKubernetesAlertDto
from taikunpycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = taikunpycore.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with taikunpycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = taikunpycore.KubernetesApi(api_client)
    alert_id = 56 # int | 
    update_kubernetes_alert_dto = taikunpycore.UpdateKubernetesAlertDto() # UpdateKubernetesAlertDto |  (optional)

    try:
        # Update k8s alert
        api_response = api_instance.kubernetes_update_alert(alert_id, update_kubernetes_alert_dto=update_kubernetes_alert_dto)
        print("The response of KubernetesApi->kubernetes_update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_update_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**|  | 
 **update_kubernetes_alert_dto** | [**UpdateKubernetesAlertDto**](UpdateKubernetesAlertDto.md)|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

