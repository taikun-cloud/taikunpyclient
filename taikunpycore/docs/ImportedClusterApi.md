# taikunpycore.ImportedClusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imported_cluster_as_cloud_credential**](ImportedClusterApi.md#imported_cluster_as_cloud_credential) | **GET** /api/v1/imported-cluster/as-cloud-credential/{projectId} | Imported cluster as cloud credential
[**imported_cluster_as_fully_managed**](ImportedClusterApi.md#imported_cluster_as_fully_managed) | **GET** /api/v1/imported-cluster/as-fully-managed/{projectId} | Imported cluster as fully managed
[**imported_cluster_as_read_only**](ImportedClusterApi.md#imported_cluster_as_read_only) | **GET** /api/v1/imported-cluster/as-read-only/{projectId} | Imported cluster as read only
[**imported_cluster_delete**](ImportedClusterApi.md#imported_cluster_delete) | **POST** /api/v1/imported-cluster/delete | Delete imported cluster
[**imported_cluster_details**](ImportedClusterApi.md#imported_cluster_details) | **GET** /api/v1/imported-cluster/{id} | Retrieve imported-cluster by given id
[**imported_cluster_disable_ai**](ImportedClusterApi.md#imported_cluster_disable_ai) | **POST** /api/v1/imported-cluster/disable-ai | Disable ai for imported cluster
[**imported_cluster_disable_backup**](ImportedClusterApi.md#imported_cluster_disable_backup) | **POST** /api/v1/imported-cluster/disable-backup | Disable backup for imported cluster
[**imported_cluster_disable_monitoring**](ImportedClusterApi.md#imported_cluster_disable_monitoring) | **POST** /api/v1/imported-cluster/disable-monitoring | Disable monitoring for imported cluster
[**imported_cluster_disable_opa**](ImportedClusterApi.md#imported_cluster_disable_opa) | **POST** /api/v1/imported-cluster/disable-opa | Disable opa for imported cluster
[**imported_cluster_enable_ai**](ImportedClusterApi.md#imported_cluster_enable_ai) | **POST** /api/v1/imported-cluster/enable-ai | Enable ai for imported cluster
[**imported_cluster_enable_backup**](ImportedClusterApi.md#imported_cluster_enable_backup) | **POST** /api/v1/imported-cluster/enable-backup | Enable backup for imported cluster
[**imported_cluster_enable_monitoring**](ImportedClusterApi.md#imported_cluster_enable_monitoring) | **POST** /api/v1/imported-cluster/enable-monitoring | Enable monitoring for imported cluster
[**imported_cluster_enable_opa**](ImportedClusterApi.md#imported_cluster_enable_opa) | **POST** /api/v1/imported-cluster/enable-opa | Enable opa for imported cluster


# **imported_cluster_as_cloud_credential**
> ImportedAsCloudCredentialList imported_cluster_as_cloud_credential(project_id)

Imported cluster as cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_as_cloud_credential_list import ImportedAsCloudCredentialList
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    project_id = 56 # int | 

    try:
        # Imported cluster as cloud credential
        api_response = api_instance.imported_cluster_as_cloud_credential(project_id)
        print("The response of ImportedClusterApi->imported_cluster_as_cloud_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_as_cloud_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**ImportedAsCloudCredentialList**](ImportedAsCloudCredentialList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imported_cluster_as_fully_managed**
> ImportedAsFullyManagedList imported_cluster_as_fully_managed(project_id)

Imported cluster as fully managed

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_as_fully_managed_list import ImportedAsFullyManagedList
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    project_id = 56 # int | 

    try:
        # Imported cluster as fully managed
        api_response = api_instance.imported_cluster_as_fully_managed(project_id)
        print("The response of ImportedClusterApi->imported_cluster_as_fully_managed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_as_fully_managed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**ImportedAsFullyManagedList**](ImportedAsFullyManagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imported_cluster_as_read_only**
> ImportedAsReadOnlyList imported_cluster_as_read_only(project_id)

Imported cluster as read only

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_as_read_only_list import ImportedAsReadOnlyList
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    project_id = 56 # int | 

    try:
        # Imported cluster as read only
        api_response = api_instance.imported_cluster_as_read_only(project_id)
        print("The response of ImportedClusterApi->imported_cluster_as_read_only:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_as_read_only: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**ImportedAsReadOnlyList**](ImportedAsReadOnlyList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imported_cluster_delete**
> object imported_cluster_delete(delete_imported_project_command)

Delete imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_imported_project_command import DeleteImportedProjectCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    delete_imported_project_command = taikunpycore.DeleteImportedProjectCommand() # DeleteImportedProjectCommand | 

    try:
        # Delete imported cluster
        api_response = api_instance.imported_cluster_delete(delete_imported_project_command)
        print("The response of ImportedClusterApi->imported_cluster_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_imported_project_command** | [**DeleteImportedProjectCommand**](DeleteImportedProjectCommand.md)|  | 

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

# **imported_cluster_details**
> ImportedClusterList imported_cluster_details(id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id)

Retrieve imported-cluster by given id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_list import ImportedClusterList
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)

    try:
        # Retrieve imported-cluster by given id
        api_response = api_instance.imported_cluster_details(id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id)
        print("The response of ImportedClusterApi->imported_cluster_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 

### Return type

[**ImportedClusterList**](ImportedClusterList.md)

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

# **imported_cluster_disable_ai**
> object imported_cluster_disable_ai(imported_cluster_disable_ai_command)

Disable ai for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_disable_ai_command import ImportedClusterDisableAiCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_disable_ai_command = taikunpycore.ImportedClusterDisableAiCommand() # ImportedClusterDisableAiCommand | 

    try:
        # Disable ai for imported cluster
        api_response = api_instance.imported_cluster_disable_ai(imported_cluster_disable_ai_command)
        print("The response of ImportedClusterApi->imported_cluster_disable_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_disable_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_disable_ai_command** | [**ImportedClusterDisableAiCommand**](ImportedClusterDisableAiCommand.md)|  | 

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

# **imported_cluster_disable_backup**
> object imported_cluster_disable_backup(imported_cluster_disable_backup_command)

Disable backup for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_disable_backup_command import ImportedClusterDisableBackupCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_disable_backup_command = taikunpycore.ImportedClusterDisableBackupCommand() # ImportedClusterDisableBackupCommand | 

    try:
        # Disable backup for imported cluster
        api_response = api_instance.imported_cluster_disable_backup(imported_cluster_disable_backup_command)
        print("The response of ImportedClusterApi->imported_cluster_disable_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_disable_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_disable_backup_command** | [**ImportedClusterDisableBackupCommand**](ImportedClusterDisableBackupCommand.md)|  | 

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

# **imported_cluster_disable_monitoring**
> object imported_cluster_disable_monitoring(imported_cluster_disable_monitoring_command)

Disable monitoring for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_disable_monitoring_command import ImportedClusterDisableMonitoringCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_disable_monitoring_command = taikunpycore.ImportedClusterDisableMonitoringCommand() # ImportedClusterDisableMonitoringCommand | 

    try:
        # Disable monitoring for imported cluster
        api_response = api_instance.imported_cluster_disable_monitoring(imported_cluster_disable_monitoring_command)
        print("The response of ImportedClusterApi->imported_cluster_disable_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_disable_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_disable_monitoring_command** | [**ImportedClusterDisableMonitoringCommand**](ImportedClusterDisableMonitoringCommand.md)|  | 

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

# **imported_cluster_disable_opa**
> object imported_cluster_disable_opa(imported_cluster_disable_opa_command)

Disable opa for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_disable_opa_command import ImportedClusterDisableOpaCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_disable_opa_command = taikunpycore.ImportedClusterDisableOpaCommand() # ImportedClusterDisableOpaCommand | 

    try:
        # Disable opa for imported cluster
        api_response = api_instance.imported_cluster_disable_opa(imported_cluster_disable_opa_command)
        print("The response of ImportedClusterApi->imported_cluster_disable_opa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_disable_opa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_disable_opa_command** | [**ImportedClusterDisableOpaCommand**](ImportedClusterDisableOpaCommand.md)|  | 

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

# **imported_cluster_enable_ai**
> object imported_cluster_enable_ai(imported_cluster_enable_ai_command)

Enable ai for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_enable_ai_command import ImportedClusterEnableAiCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_enable_ai_command = taikunpycore.ImportedClusterEnableAiCommand() # ImportedClusterEnableAiCommand | 

    try:
        # Enable ai for imported cluster
        api_response = api_instance.imported_cluster_enable_ai(imported_cluster_enable_ai_command)
        print("The response of ImportedClusterApi->imported_cluster_enable_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_enable_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_enable_ai_command** | [**ImportedClusterEnableAiCommand**](ImportedClusterEnableAiCommand.md)|  | 

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

# **imported_cluster_enable_backup**
> object imported_cluster_enable_backup(imported_cluster_enable_backup_command)

Enable backup for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_enable_backup_command import ImportedClusterEnableBackupCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_enable_backup_command = taikunpycore.ImportedClusterEnableBackupCommand() # ImportedClusterEnableBackupCommand | 

    try:
        # Enable backup for imported cluster
        api_response = api_instance.imported_cluster_enable_backup(imported_cluster_enable_backup_command)
        print("The response of ImportedClusterApi->imported_cluster_enable_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_enable_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_enable_backup_command** | [**ImportedClusterEnableBackupCommand**](ImportedClusterEnableBackupCommand.md)|  | 

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

# **imported_cluster_enable_monitoring**
> object imported_cluster_enable_monitoring(imported_cluster_enable_monitoring_command)

Enable monitoring for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_enable_monitoring_command import ImportedClusterEnableMonitoringCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_enable_monitoring_command = taikunpycore.ImportedClusterEnableMonitoringCommand() # ImportedClusterEnableMonitoringCommand | 

    try:
        # Enable monitoring for imported cluster
        api_response = api_instance.imported_cluster_enable_monitoring(imported_cluster_enable_monitoring_command)
        print("The response of ImportedClusterApi->imported_cluster_enable_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_enable_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_enable_monitoring_command** | [**ImportedClusterEnableMonitoringCommand**](ImportedClusterEnableMonitoringCommand.md)|  | 

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

# **imported_cluster_enable_opa**
> object imported_cluster_enable_opa(imported_cluster_enable_opa_command)

Enable opa for imported cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.imported_cluster_enable_opa_command import ImportedClusterEnableOpaCommand
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
    api_instance = taikunpycore.ImportedClusterApi(api_client)
    imported_cluster_enable_opa_command = taikunpycore.ImportedClusterEnableOpaCommand() # ImportedClusterEnableOpaCommand | 

    try:
        # Enable opa for imported cluster
        api_response = api_instance.imported_cluster_enable_opa(imported_cluster_enable_opa_command)
        print("The response of ImportedClusterApi->imported_cluster_enable_opa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedClusterApi->imported_cluster_enable_opa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_cluster_enable_opa_command** | [**ImportedClusterEnableOpaCommand**](ImportedClusterEnableOpaCommand.md)|  | 

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

