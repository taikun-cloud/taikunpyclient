# taikunpycore.ProjectDeploymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_deployment_commit**](ProjectDeploymentApi.md#project_deployment_commit) | **POST** /api/v1/project-deployment/commit | Commit
[**project_deployment_commit_vm**](ProjectDeploymentApi.md#project_deployment_commit_vm) | **POST** /api/v1/project-deployment/commit-vm | Commit
[**project_deployment_completed**](ProjectDeploymentApi.md#project_deployment_completed) | **POST** /api/v1/project-deployment/completed | Update project fields
[**project_deployment_delete**](ProjectDeploymentApi.md#project_deployment_delete) | **POST** /api/v1/project-deployment/delete | Delete
[**project_deployment_delete_vm_disks**](ProjectDeploymentApi.md#project_deployment_delete_vm_disks) | **POST** /api/v1/project-deployment/delete-vm-disks | Delete vm disks
[**project_deployment_delete_vms**](ProjectDeploymentApi.md#project_deployment_delete_vms) | **POST** /api/v1/project-deployment/delete-vms | Delete vms
[**project_deployment_disable_ai**](ProjectDeploymentApi.md#project_deployment_disable_ai) | **POST** /api/v1/project-deployment/disable-ai | Disable ai
[**project_deployment_disable_backup**](ProjectDeploymentApi.md#project_deployment_disable_backup) | **POST** /api/v1/project-deployment/disable-backup | Disable backup
[**project_deployment_disable_monitoring**](ProjectDeploymentApi.md#project_deployment_disable_monitoring) | **POST** /api/v1/project-deployment/disable-monitoring | Disable monitoring
[**project_deployment_disable_opa**](ProjectDeploymentApi.md#project_deployment_disable_opa) | **POST** /api/v1/project-deployment/disable-opa | Disable opa
[**project_deployment_enable_ai**](ProjectDeploymentApi.md#project_deployment_enable_ai) | **POST** /api/v1/project-deployment/enable-ai | Enable ai
[**project_deployment_enable_backup**](ProjectDeploymentApi.md#project_deployment_enable_backup) | **POST** /api/v1/project-deployment/enable-backup | Enable backup
[**project_deployment_enable_monitoring**](ProjectDeploymentApi.md#project_deployment_enable_monitoring) | **POST** /api/v1/project-deployment/enable-monitoring | Enable monitoring
[**project_deployment_enable_opa**](ProjectDeploymentApi.md#project_deployment_enable_opa) | **POST** /api/v1/project-deployment/enable-opa | Enable opa
[**project_deployment_import_cluster**](ProjectDeploymentApi.md#project_deployment_import_cluster) | **POST** /api/v1/project-deployment/import-cluster | Import cluster
[**project_deployment_repair**](ProjectDeploymentApi.md#project_deployment_repair) | **POST** /api/v1/project-deployment/repair | Repair
[**project_deployment_repair_vm**](ProjectDeploymentApi.md#project_deployment_repair_vm) | **POST** /api/v1/project-deployment/repair-vm | Repair Vm
[**project_deployment_tofu_migrate**](ProjectDeploymentApi.md#project_deployment_tofu_migrate) | **POST** /api/v1/project-deployment/tofu-migrate | Tofu migrate
[**project_deployment_update**](ProjectDeploymentApi.md#project_deployment_update) | **POST** /api/v1/project-deployment/update | Update stage of project
[**project_deployment_upgrade**](ProjectDeploymentApi.md#project_deployment_upgrade) | **POST** /api/v1/project-deployment/upgrade/{projectId} | Upgrade the project&#39;s Kubernetes to the next available version. Project must be READY.


# **project_deployment_commit**
> object project_deployment_commit(project_deployment_commit_command=project_deployment_commit_command)

Commit

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_deployment_commit_command import ProjectDeploymentCommitCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    project_deployment_commit_command = taikunpycore.ProjectDeploymentCommitCommand() # ProjectDeploymentCommitCommand |  (optional)

    try:
        # Commit
        api_response = api_instance.project_deployment_commit(project_deployment_commit_command=project_deployment_commit_command)
        print("The response of ProjectDeploymentApi->project_deployment_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment_commit_command** | [**ProjectDeploymentCommitCommand**](ProjectDeploymentCommitCommand.md)|  | [optional] 

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

# **project_deployment_commit_vm**
> object project_deployment_commit_vm(deployment_commit_vm_command)

Commit

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_commit_vm_command import DeploymentCommitVmCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_commit_vm_command = taikunpycore.DeploymentCommitVmCommand() # DeploymentCommitVmCommand | 

    try:
        # Commit
        api_response = api_instance.project_deployment_commit_vm(deployment_commit_vm_command)
        print("The response of ProjectDeploymentApi->project_deployment_commit_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_commit_vm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_commit_vm_command** | [**DeploymentCommitVmCommand**](DeploymentCommitVmCommand.md)|  | 

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

# **project_deployment_completed**
> object project_deployment_completed(deployment_completed_command=deployment_completed_command)

Update project fields

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_completed_command import DeploymentCompletedCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_completed_command = taikunpycore.DeploymentCompletedCommand() # DeploymentCompletedCommand |  (optional)

    try:
        # Update project fields
        api_response = api_instance.project_deployment_completed(deployment_completed_command=deployment_completed_command)
        print("The response of ProjectDeploymentApi->project_deployment_completed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_completed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_completed_command** | [**DeploymentCompletedCommand**](DeploymentCompletedCommand.md)|  | [optional] 

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

# **project_deployment_delete**
> object project_deployment_delete(project_deployment_delete_servers_command)

Delete

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_deployment_delete_servers_command import ProjectDeploymentDeleteServersCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    project_deployment_delete_servers_command = taikunpycore.ProjectDeploymentDeleteServersCommand() # ProjectDeploymentDeleteServersCommand | 

    try:
        # Delete
        api_response = api_instance.project_deployment_delete(project_deployment_delete_servers_command)
        print("The response of ProjectDeploymentApi->project_deployment_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment_delete_servers_command** | [**ProjectDeploymentDeleteServersCommand**](ProjectDeploymentDeleteServersCommand.md)|  | 

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

# **project_deployment_delete_vm_disks**
> object project_deployment_delete_vm_disks(delete_vm_disk_command=delete_vm_disk_command)

Delete vm disks

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_vm_disk_command import DeleteVmDiskCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    delete_vm_disk_command = taikunpycore.DeleteVmDiskCommand() # DeleteVmDiskCommand |  (optional)

    try:
        # Delete vm disks
        api_response = api_instance.project_deployment_delete_vm_disks(delete_vm_disk_command=delete_vm_disk_command)
        print("The response of ProjectDeploymentApi->project_deployment_delete_vm_disks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_delete_vm_disks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_vm_disk_command** | [**DeleteVmDiskCommand**](DeleteVmDiskCommand.md)|  | [optional] 

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

# **project_deployment_delete_vms**
> object project_deployment_delete_vms(project_deployment_delete_vms_command)

Delete vms

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_deployment_delete_vms_command import ProjectDeploymentDeleteVmsCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    project_deployment_delete_vms_command = taikunpycore.ProjectDeploymentDeleteVmsCommand() # ProjectDeploymentDeleteVmsCommand | 

    try:
        # Delete vms
        api_response = api_instance.project_deployment_delete_vms(project_deployment_delete_vms_command)
        print("The response of ProjectDeploymentApi->project_deployment_delete_vms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_delete_vms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment_delete_vms_command** | [**ProjectDeploymentDeleteVmsCommand**](ProjectDeploymentDeleteVmsCommand.md)|  | 

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

# **project_deployment_disable_ai**
> object project_deployment_disable_ai(deployment_disable_ai_command)

Disable ai

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_disable_ai_command import DeploymentDisableAiCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_disable_ai_command = taikunpycore.DeploymentDisableAiCommand() # DeploymentDisableAiCommand | 

    try:
        # Disable ai
        api_response = api_instance.project_deployment_disable_ai(deployment_disable_ai_command)
        print("The response of ProjectDeploymentApi->project_deployment_disable_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_disable_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_disable_ai_command** | [**DeploymentDisableAiCommand**](DeploymentDisableAiCommand.md)|  | 

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

# **project_deployment_disable_backup**
> object project_deployment_disable_backup(deployment_disable_backup_command)

Disable backup

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_disable_backup_command import DeploymentDisableBackupCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_disable_backup_command = taikunpycore.DeploymentDisableBackupCommand() # DeploymentDisableBackupCommand | 

    try:
        # Disable backup
        api_response = api_instance.project_deployment_disable_backup(deployment_disable_backup_command)
        print("The response of ProjectDeploymentApi->project_deployment_disable_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_disable_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_disable_backup_command** | [**DeploymentDisableBackupCommand**](DeploymentDisableBackupCommand.md)|  | 

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

# **project_deployment_disable_monitoring**
> object project_deployment_disable_monitoring(deployment_disable_monitoring_command)

Disable monitoring

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_disable_monitoring_command import DeploymentDisableMonitoringCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_disable_monitoring_command = taikunpycore.DeploymentDisableMonitoringCommand() # DeploymentDisableMonitoringCommand | 

    try:
        # Disable monitoring
        api_response = api_instance.project_deployment_disable_monitoring(deployment_disable_monitoring_command)
        print("The response of ProjectDeploymentApi->project_deployment_disable_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_disable_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_disable_monitoring_command** | [**DeploymentDisableMonitoringCommand**](DeploymentDisableMonitoringCommand.md)|  | 

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

# **project_deployment_disable_opa**
> object project_deployment_disable_opa(deployment_disable_opa_command)

Disable opa

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_disable_opa_command import DeploymentDisableOpaCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_disable_opa_command = taikunpycore.DeploymentDisableOpaCommand() # DeploymentDisableOpaCommand | 

    try:
        # Disable opa
        api_response = api_instance.project_deployment_disable_opa(deployment_disable_opa_command)
        print("The response of ProjectDeploymentApi->project_deployment_disable_opa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_disable_opa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_disable_opa_command** | [**DeploymentDisableOpaCommand**](DeploymentDisableOpaCommand.md)|  | 

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

# **project_deployment_enable_ai**
> object project_deployment_enable_ai(deployment_enable_ai_command)

Enable ai

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_enable_ai_command import DeploymentEnableAiCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_enable_ai_command = taikunpycore.DeploymentEnableAiCommand() # DeploymentEnableAiCommand | 

    try:
        # Enable ai
        api_response = api_instance.project_deployment_enable_ai(deployment_enable_ai_command)
        print("The response of ProjectDeploymentApi->project_deployment_enable_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_enable_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_enable_ai_command** | [**DeploymentEnableAiCommand**](DeploymentEnableAiCommand.md)|  | 

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

# **project_deployment_enable_backup**
> object project_deployment_enable_backup(deployment_enable_backup_command)

Enable backup

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_enable_backup_command import DeploymentEnableBackupCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_enable_backup_command = taikunpycore.DeploymentEnableBackupCommand() # DeploymentEnableBackupCommand | 

    try:
        # Enable backup
        api_response = api_instance.project_deployment_enable_backup(deployment_enable_backup_command)
        print("The response of ProjectDeploymentApi->project_deployment_enable_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_enable_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_enable_backup_command** | [**DeploymentEnableBackupCommand**](DeploymentEnableBackupCommand.md)|  | 

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

# **project_deployment_enable_monitoring**
> object project_deployment_enable_monitoring(deployment_enable_monitoring_command)

Enable monitoring

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_enable_monitoring_command import DeploymentEnableMonitoringCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_enable_monitoring_command = taikunpycore.DeploymentEnableMonitoringCommand() # DeploymentEnableMonitoringCommand | 

    try:
        # Enable monitoring
        api_response = api_instance.project_deployment_enable_monitoring(deployment_enable_monitoring_command)
        print("The response of ProjectDeploymentApi->project_deployment_enable_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_enable_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_enable_monitoring_command** | [**DeploymentEnableMonitoringCommand**](DeploymentEnableMonitoringCommand.md)|  | 

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

# **project_deployment_enable_opa**
> object project_deployment_enable_opa(deployment_opa_enable_command)

Enable opa

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.deployment_opa_enable_command import DeploymentOpaEnableCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    deployment_opa_enable_command = taikunpycore.DeploymentOpaEnableCommand() # DeploymentOpaEnableCommand | 

    try:
        # Enable opa
        api_response = api_instance.project_deployment_enable_opa(deployment_opa_enable_command)
        print("The response of ProjectDeploymentApi->project_deployment_enable_opa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_enable_opa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_opa_enable_command** | [**DeploymentOpaEnableCommand**](DeploymentOpaEnableCommand.md)|  | 

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

# **project_deployment_import_cluster**
> object project_deployment_import_cluster(name, config=config, is_taikun_ingress_controller=is_taikun_ingress_controller, is_existing_ingress_controller=is_existing_ingress_controller, ingress_class=ingress_class, ingress_host=ingress_host, continent=continent, import_type=import_type, organization_id=organization_id, cloud_id=cloud_id, import_cluster_name=import_cluster_name, resource_group_name=resource_group_name, region=region)

Import cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.e_import_cluster_type import EImportClusterType
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    name = 'name_example' # str | 
    config = None # bytearray |  (optional)
    is_taikun_ingress_controller = True # bool |  (optional)
    is_existing_ingress_controller = True # bool |  (optional)
    ingress_class = 'ingress_class_example' # str |  (optional)
    ingress_host = 'ingress_host_example' # str |  (optional)
    continent = 'continent_example' # str |  (optional)
    import_type = taikunpycore.EImportClusterType() # EImportClusterType |  (optional)
    organization_id = 56 # int |  (optional)
    cloud_id = 56 # int |  (optional)
    import_cluster_name = 'import_cluster_name_example' # str |  (optional)
    resource_group_name = 'resource_group_name_example' # str |  (optional)
    region = 'region_example' # str |  (optional)

    try:
        # Import cluster
        api_response = api_instance.project_deployment_import_cluster(name, config=config, is_taikun_ingress_controller=is_taikun_ingress_controller, is_existing_ingress_controller=is_existing_ingress_controller, ingress_class=ingress_class, ingress_host=ingress_host, continent=continent, import_type=import_type, organization_id=organization_id, cloud_id=cloud_id, import_cluster_name=import_cluster_name, resource_group_name=resource_group_name, region=region)
        print("The response of ProjectDeploymentApi->project_deployment_import_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_import_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **config** | **bytearray**|  | [optional] 
 **is_taikun_ingress_controller** | **bool**|  | [optional] 
 **is_existing_ingress_controller** | **bool**|  | [optional] 
 **ingress_class** | **str**|  | [optional] 
 **ingress_host** | **str**|  | [optional] 
 **continent** | **str**|  | [optional] 
 **import_type** | [**EImportClusterType**](EImportClusterType.md)|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **cloud_id** | **int**|  | [optional] 
 **import_cluster_name** | **str**|  | [optional] 
 **resource_group_name** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **project_deployment_repair**
> object project_deployment_repair(project_deployment_repair_command)

Repair

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_deployment_repair_command import ProjectDeploymentRepairCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    project_deployment_repair_command = taikunpycore.ProjectDeploymentRepairCommand() # ProjectDeploymentRepairCommand | 

    try:
        # Repair
        api_response = api_instance.project_deployment_repair(project_deployment_repair_command)
        print("The response of ProjectDeploymentApi->project_deployment_repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_repair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment_repair_command** | [**ProjectDeploymentRepairCommand**](ProjectDeploymentRepairCommand.md)|  | 

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

# **project_deployment_repair_vm**
> object project_deployment_repair_vm(project_deployment_repair_vm_command)

Repair Vm

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_deployment_repair_vm_command import ProjectDeploymentRepairVmCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    project_deployment_repair_vm_command = taikunpycore.ProjectDeploymentRepairVmCommand() # ProjectDeploymentRepairVmCommand | 

    try:
        # Repair Vm
        api_response = api_instance.project_deployment_repair_vm(project_deployment_repair_vm_command)
        print("The response of ProjectDeploymentApi->project_deployment_repair_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_repair_vm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment_repair_vm_command** | [**ProjectDeploymentRepairVmCommand**](ProjectDeploymentRepairVmCommand.md)|  | 

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

# **project_deployment_tofu_migrate**
> object project_deployment_tofu_migrate(tofu_migrate_command)

Tofu migrate

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.tofu_migrate_command import TofuMigrateCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    tofu_migrate_command = taikunpycore.TofuMigrateCommand() # TofuMigrateCommand | 

    try:
        # Tofu migrate
        api_response = api_instance.project_deployment_tofu_migrate(tofu_migrate_command)
        print("The response of ProjectDeploymentApi->project_deployment_tofu_migrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_tofu_migrate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tofu_migrate_command** | [**TofuMigrateCommand**](TofuMigrateCommand.md)|  | 

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

# **project_deployment_update**
> object project_deployment_update(update_stage_command=update_stage_command)

Update stage of project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_stage_command import UpdateStageCommand
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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    update_stage_command = taikunpycore.UpdateStageCommand() # UpdateStageCommand |  (optional)

    try:
        # Update stage of project
        api_response = api_instance.project_deployment_update(update_stage_command=update_stage_command)
        print("The response of ProjectDeploymentApi->project_deployment_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_stage_command** | [**UpdateStageCommand**](UpdateStageCommand.md)|  | [optional] 

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

# **project_deployment_upgrade**
> object project_deployment_upgrade(project_id)

Upgrade the project's Kubernetes to the next available version. Project must be READY.

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
    api_instance = taikunpycore.ProjectDeploymentApi(api_client)
    project_id = 56 # int | 

    try:
        # Upgrade the project's Kubernetes to the next available version. Project must be READY.
        api_response = api_instance.project_deployment_upgrade(project_id)
        print("The response of ProjectDeploymentApi->project_deployment_upgrade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->project_deployment_upgrade: %s\n" % e)
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

