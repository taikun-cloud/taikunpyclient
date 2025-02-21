# taikunpycore.KubeConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kubeconfig_create**](KubeConfigApi.md#kubeconfig_create) | **POST** /api/v1/kubeconfig | Create kube config
[**kubeconfig_delete**](KubeConfigApi.md#kubeconfig_delete) | **POST** /api/v1/kubeconfig/delete | Delete kube config
[**kubeconfig_delete_by_project_id**](KubeConfigApi.md#kubeconfig_delete_by_project_id) | **POST** /api/v1/kubeconfig/delete-by-project-id | Delete kube config by project id
[**kubeconfig_download**](KubeConfigApi.md#kubeconfig_download) | **POST** /api/v1/kubeconfig/download | Download kube config file for user by project Id
[**kubeconfig_export**](KubeConfigApi.md#kubeconfig_export) | **POST** /api/v1/kubeconfig/export | Export
[**kubeconfig_interactive_shell**](KubeConfigApi.md#kubeconfig_interactive_shell) | **POST** /api/v1/kubeconfig/interactive-shell | Interactive shell for user kube config
[**kubeconfig_list**](KubeConfigApi.md#kubeconfig_list) | **GET** /api/v1/kubeconfig | Retrieve a list of kube configs for project


# **kubeconfig_create**
> ApiResponse kubeconfig_create(create_kube_config_command=create_kube_config_command)

Create kube config

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_kube_config_command import CreateKubeConfigCommand
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    create_kube_config_command = taikunpycore.CreateKubeConfigCommand() # CreateKubeConfigCommand |  (optional)

    try:
        # Create kube config
        api_response = api_instance.kubeconfig_create(create_kube_config_command=create_kube_config_command)
        print("The response of KubeConfigApi->kubeconfig_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_kube_config_command** | [**CreateKubeConfigCommand**](CreateKubeConfigCommand.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **kubeconfig_delete**
> object kubeconfig_delete(delete_kube_config_command)

Delete kube config

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_kube_config_command import DeleteKubeConfigCommand
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    delete_kube_config_command = taikunpycore.DeleteKubeConfigCommand() # DeleteKubeConfigCommand | 

    try:
        # Delete kube config
        api_response = api_instance.kubeconfig_delete(delete_kube_config_command)
        print("The response of KubeConfigApi->kubeconfig_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_kube_config_command** | [**DeleteKubeConfigCommand**](DeleteKubeConfigCommand.md)|  | 

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

# **kubeconfig_delete_by_project_id**
> object kubeconfig_delete_by_project_id(delete_kube_config_by_project_id_command)

Delete kube config by project id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_kube_config_by_project_id_command import DeleteKubeConfigByProjectIdCommand
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    delete_kube_config_by_project_id_command = taikunpycore.DeleteKubeConfigByProjectIdCommand() # DeleteKubeConfigByProjectIdCommand | 

    try:
        # Delete kube config by project id
        api_response = api_instance.kubeconfig_delete_by_project_id(delete_kube_config_by_project_id_command)
        print("The response of KubeConfigApi->kubeconfig_delete_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_delete_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_kube_config_by_project_id_command** | [**DeleteKubeConfigByProjectIdCommand**](DeleteKubeConfigByProjectIdCommand.md)|  | 

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

# **kubeconfig_download**
> str kubeconfig_download(download_kube_config_command)

Download kube config file for user by project Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.download_kube_config_command import DownloadKubeConfigCommand
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    download_kube_config_command = taikunpycore.DownloadKubeConfigCommand() # DownloadKubeConfigCommand | 

    try:
        # Download kube config file for user by project Id
        api_response = api_instance.kubeconfig_download(download_kube_config_command)
        print("The response of KubeConfigApi->kubeconfig_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_kube_config_command** | [**DownloadKubeConfigCommand**](DownloadKubeConfigCommand.md)|  | 

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

# **kubeconfig_export**
> CsvExporter kubeconfig_export(export_kube_config_command)

Export

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.csv_exporter import CsvExporter
from taikunpycore.models.export_kube_config_command import ExportKubeConfigCommand
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    export_kube_config_command = taikunpycore.ExportKubeConfigCommand() # ExportKubeConfigCommand | 

    try:
        # Export
        api_response = api_instance.kubeconfig_export(export_kube_config_command)
        print("The response of KubeConfigApi->kubeconfig_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_kube_config_command** | [**ExportKubeConfigCommand**](ExportKubeConfigCommand.md)|  | 

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

# **kubeconfig_interactive_shell**
> InteractiveShellDto kubeconfig_interactive_shell(kube_config_interactive_shell_command)

Interactive shell for user kube config

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.interactive_shell_dto import InteractiveShellDto
from taikunpycore.models.kube_config_interactive_shell_command import KubeConfigInteractiveShellCommand
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    kube_config_interactive_shell_command = taikunpycore.KubeConfigInteractiveShellCommand() # KubeConfigInteractiveShellCommand | 

    try:
        # Interactive shell for user kube config
        api_response = api_instance.kubeconfig_interactive_shell(kube_config_interactive_shell_command)
        print("The response of KubeConfigApi->kubeconfig_interactive_shell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_interactive_shell: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kube_config_interactive_shell_command** | [**KubeConfigInteractiveShellCommand**](KubeConfigInteractiveShellCommand.md)|  | 

### Return type

[**InteractiveShellDto**](InteractiveShellDto.md)

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

# **kubeconfig_list**
> KubeConfigForUserList kubeconfig_list(project_id, organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id)

Retrieve a list of kube configs for project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kube_config_for_user_list import KubeConfigForUserList
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
    api_instance = taikunpycore.KubeConfigApi(api_client)
    project_id = 56 # int | 
    organization_id = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve a list of kube configs for project
        api_response = api_instance.kubeconfig_list(project_id, organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id)
        print("The response of KubeConfigApi->kubeconfig_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubeConfigApi->kubeconfig_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **organization_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**KubeConfigForUserList**](KubeConfigForUserList.md)

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

