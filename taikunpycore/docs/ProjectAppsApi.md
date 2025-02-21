# taikunpycore.ProjectAppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectapp_autosync**](ProjectAppsApi.md#projectapp_autosync) | **POST** /api/v1/projectapp/autosync | AutoSync management
[**projectapp_cancel**](ProjectAppsApi.md#projectapp_cancel) | **POST** /api/v1/projectapp/cancel | Cancel an application
[**projectapp_delete**](ProjectAppsApi.md#projectapp_delete) | **DELETE** /api/v1/projectapp/uninstall/{projectAppId} | Uninstall application
[**projectapp_details**](ProjectAppsApi.md#projectapp_details) | **GET** /api/v1/projectapp/{id} | Retrieve project app&#39;s details
[**projectapp_install**](ProjectAppsApi.md#projectapp_install) | **POST** /api/v1/projectapp/install | Install an application
[**projectapp_list**](ProjectAppsApi.md#projectapp_list) | **GET** /api/v1/projectapp/list | Retrieve all project apps according to current organization
[**projectapp_lock_manager**](ProjectAppsApi.md#projectapp_lock_manager) | **POST** /api/v1/projectapp/lockmanager | Lock/Unlock project app
[**projectapp_sync**](ProjectAppsApi.md#projectapp_sync) | **POST** /api/v1/projectapp/sync | Sync an application
[**projectapp_update**](ProjectAppsApi.md#projectapp_update) | **POST** /api/v1/projectapp/update | Update project app
[**projectapp_update_extra_values**](ProjectAppsApi.md#projectapp_update_extra_values) | **POST** /api/v1/projectapp/update-extra-values | Update extra values


# **projectapp_autosync**
> object projectapp_autosync(auto_sync_management_command)

AutoSync management

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.auto_sync_management_command import AutoSyncManagementCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    auto_sync_management_command = taikunpycore.AutoSyncManagementCommand() # AutoSyncManagementCommand | 

    try:
        # AutoSync management
        api_response = api_instance.projectapp_autosync(auto_sync_management_command)
        print("The response of ProjectAppsApi->projectapp_autosync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_autosync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_sync_management_command** | [**AutoSyncManagementCommand**](AutoSyncManagementCommand.md)|  | 

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

# **projectapp_cancel**
> object projectapp_cancel(cancel_project_app_command)

Cancel an application

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.cancel_project_app_command import CancelProjectAppCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    cancel_project_app_command = taikunpycore.CancelProjectAppCommand() # CancelProjectAppCommand | 

    try:
        # Cancel an application
        api_response = api_instance.projectapp_cancel(cancel_project_app_command)
        print("The response of ProjectAppsApi->projectapp_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_project_app_command** | [**CancelProjectAppCommand**](CancelProjectAppCommand.md)|  | 

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

# **projectapp_delete**
> projectapp_delete(project_app_id)

Uninstall application

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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    project_app_id = 56 # int | 

    try:
        # Uninstall application
        api_instance.projectapp_delete(project_app_id)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_app_id** | **int**|  | 

### Return type

void (empty response body)

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

# **projectapp_details**
> ProjectAppDetailsDto projectapp_details(id)

Retrieve project app's details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_app_details_dto import ProjectAppDetailsDto
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve project app's details
        api_response = api_instance.projectapp_details(id)
        print("The response of ProjectAppsApi->projectapp_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProjectAppDetailsDto**](ProjectAppDetailsDto.md)

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

# **projectapp_install**
> ApiResponse projectapp_install(create_project_app_command=create_project_app_command)

Install an application

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_project_app_command import CreateProjectAppCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    create_project_app_command = taikunpycore.CreateProjectAppCommand() # CreateProjectAppCommand |  (optional)

    try:
        # Install an application
        api_response = api_instance.projectapp_install(create_project_app_command=create_project_app_command)
        print("The response of ProjectAppsApi->projectapp_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_app_command** | [**CreateProjectAppCommand**](CreateProjectAppCommand.md)|  | [optional] 

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

# **projectapp_list**
> ProjectAppList projectapp_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, project_id=project_id, organization_id=organization_id)

Retrieve all project apps according to current organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.project_app_list import ProjectAppList
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 56 # int |  (optional)
    project_id = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve all project apps according to current organization
        api_response = api_instance.projectapp_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, project_id=project_id, organization_id=organization_id)
        print("The response of ProjectAppsApi->projectapp_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**ProjectAppList**](ProjectAppList.md)

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

# **projectapp_lock_manager**
> object projectapp_lock_manager(lock_project_app_command)

Lock/Unlock project app

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.lock_project_app_command import LockProjectAppCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    lock_project_app_command = taikunpycore.LockProjectAppCommand() # LockProjectAppCommand | 

    try:
        # Lock/Unlock project app
        api_response = api_instance.projectapp_lock_manager(lock_project_app_command)
        print("The response of ProjectAppsApi->projectapp_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_project_app_command** | [**LockProjectAppCommand**](LockProjectAppCommand.md)|  | 

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

# **projectapp_sync**
> object projectapp_sync(sync_project_app_command)

Sync an application

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.sync_project_app_command import SyncProjectAppCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    sync_project_app_command = taikunpycore.SyncProjectAppCommand() # SyncProjectAppCommand | 

    try:
        # Sync an application
        api_response = api_instance.projectapp_sync(sync_project_app_command)
        print("The response of ProjectAppsApi->projectapp_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_project_app_command** | [**SyncProjectAppCommand**](SyncProjectAppCommand.md)|  | 

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

# **projectapp_update**
> object projectapp_update(update_project_app_command)

Update project app

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_project_app_command import UpdateProjectAppCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    update_project_app_command = taikunpycore.UpdateProjectAppCommand() # UpdateProjectAppCommand | 

    try:
        # Update project app
        api_response = api_instance.projectapp_update(update_project_app_command)
        print("The response of ProjectAppsApi->projectapp_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_project_app_command** | [**UpdateProjectAppCommand**](UpdateProjectAppCommand.md)|  | 

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

# **projectapp_update_extra_values**
> object projectapp_update_extra_values(edit_project_app_extra_values_command)

Update extra values

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_project_app_extra_values_command import EditProjectAppExtraValuesCommand
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
    api_instance = taikunpycore.ProjectAppsApi(api_client)
    edit_project_app_extra_values_command = taikunpycore.EditProjectAppExtraValuesCommand() # EditProjectAppExtraValuesCommand | 

    try:
        # Update extra values
        api_response = api_instance.projectapp_update_extra_values(edit_project_app_extra_values_command)
        print("The response of ProjectAppsApi->projectapp_update_extra_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAppsApi->projectapp_update_extra_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_project_app_extra_values_command** | [**EditProjectAppExtraValuesCommand**](EditProjectAppExtraValuesCommand.md)|  | 

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

