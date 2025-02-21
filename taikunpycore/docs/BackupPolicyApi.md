# taikunpycore.BackupPolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_by_name**](BackupPolicyApi.md#backup_by_name) | **GET** /api/v1/backup/{projectId}/{name} | Get backup info by name
[**backup_create**](BackupPolicyApi.md#backup_create) | **POST** /api/v1/backup/create | Add backup policy
[**backup_delete_backup**](BackupPolicyApi.md#backup_delete_backup) | **POST** /api/v1/backup/delete/backup | Remove policy backup
[**backup_delete_backup_location**](BackupPolicyApi.md#backup_delete_backup_location) | **POST** /api/v1/backup/delete/location | Remove backup location from project
[**backup_delete_restore**](BackupPolicyApi.md#backup_delete_restore) | **POST** /api/v1/backup/delete/restore | Remove policy restore
[**backup_delete_schedule**](BackupPolicyApi.md#backup_delete_schedule) | **POST** /api/v1/backup/delete/schedule | Remove policy schedule
[**backup_describe_backup**](BackupPolicyApi.md#backup_describe_backup) | **GET** /api/v1/backup/describe/backup/{projectId}/{name} | Get backup info by name
[**backup_describe_restore**](BackupPolicyApi.md#backup_describe_restore) | **GET** /api/v1/backup/describe/restore/{projectId}/{name} | Get restore info by name
[**backup_describe_schedule**](BackupPolicyApi.md#backup_describe_schedule) | **GET** /api/v1/backup/describe/schedule/{projectId}/{name} | Get schedule info by name
[**backup_import_backup_storage**](BackupPolicyApi.md#backup_import_backup_storage) | **POST** /api/v1/backup/location | Import backup storage from source project to target project
[**backup_list_all_backup_storages**](BackupPolicyApi.md#backup_list_all_backup_storages) | **GET** /api/v1/backup/location/{projectId} | List all backup locations
[**backup_list_all_backups**](BackupPolicyApi.md#backup_list_all_backups) | **GET** /api/v1/backup/backups/{projectId} | List all backups
[**backup_list_all_delete_backup_requests**](BackupPolicyApi.md#backup_list_all_delete_backup_requests) | **GET** /api/v1/backup/delete-requests/{projectId} | List all delete backup requests
[**backup_list_all_restores**](BackupPolicyApi.md#backup_list_all_restores) | **GET** /api/v1/backup/restores/{projectId} | List all restores
[**backup_list_all_schedules**](BackupPolicyApi.md#backup_list_all_schedules) | **GET** /api/v1/backup/schedules/{projectId} | List all schedules
[**backup_restore_backup**](BackupPolicyApi.md#backup_restore_backup) | **POST** /api/v1/backup/restore | Restore backup


# **backup_by_name**
> BackupDto backup_by_name(project_id, name)

Get backup info by name

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_dto import BackupDto
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    name = 'name_example' # str | 

    try:
        # Get backup info by name
        api_response = api_instance.backup_by_name(project_id, name)
        print("The response of BackupPolicyApi->backup_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

[**BackupDto**](BackupDto.md)

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

# **backup_create**
> object backup_create(create_backup_policy_command=create_backup_policy_command)

Add backup policy

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_backup_policy_command import CreateBackupPolicyCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    create_backup_policy_command = {"name":"taikun","includeNamespaces":["taikun.cloud/backup"],"cronPeriod":"0 0 12 * * ?","projectId":1,"retentionPeriod":"720h"} # CreateBackupPolicyCommand |  (optional)

    try:
        # Add backup policy
        api_response = api_instance.backup_create(create_backup_policy_command=create_backup_policy_command)
        print("The response of BackupPolicyApi->backup_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_backup_policy_command** | [**CreateBackupPolicyCommand**](CreateBackupPolicyCommand.md)|  | [optional] 

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

# **backup_delete_backup**
> object backup_delete_backup(delete_backup_command)

Remove policy backup

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_backup_command import DeleteBackupCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    delete_backup_command = taikunpycore.DeleteBackupCommand() # DeleteBackupCommand | 

    try:
        # Remove policy backup
        api_response = api_instance.backup_delete_backup(delete_backup_command)
        print("The response of BackupPolicyApi->backup_delete_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_delete_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_backup_command** | [**DeleteBackupCommand**](DeleteBackupCommand.md)|  | 

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

# **backup_delete_backup_location**
> object backup_delete_backup_location(delete_backup_storage_location_command=delete_backup_storage_location_command)

Remove backup location from project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_backup_storage_location_command import DeleteBackupStorageLocationCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    delete_backup_storage_location_command = {"projectId":1,"storageLocation":"taikun"} # DeleteBackupStorageLocationCommand |  (optional)

    try:
        # Remove backup location from project
        api_response = api_instance.backup_delete_backup_location(delete_backup_storage_location_command=delete_backup_storage_location_command)
        print("The response of BackupPolicyApi->backup_delete_backup_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_delete_backup_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_backup_storage_location_command** | [**DeleteBackupStorageLocationCommand**](DeleteBackupStorageLocationCommand.md)|  | [optional] 

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

# **backup_delete_restore**
> object backup_delete_restore(delete_restore_command=delete_restore_command)

Remove policy restore

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_restore_command import DeleteRestoreCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    delete_restore_command = {"projectId":1,"name":"taikun"} # DeleteRestoreCommand |  (optional)

    try:
        # Remove policy restore
        api_response = api_instance.backup_delete_restore(delete_restore_command=delete_restore_command)
        print("The response of BackupPolicyApi->backup_delete_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_delete_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_restore_command** | [**DeleteRestoreCommand**](DeleteRestoreCommand.md)|  | [optional] 

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

# **backup_delete_schedule**
> object backup_delete_schedule(delete_schedule_command=delete_schedule_command)

Remove policy schedule

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_schedule_command import DeleteScheduleCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    delete_schedule_command = {"projectId":1,"name":"taikun"} # DeleteScheduleCommand |  (optional)

    try:
        # Remove policy schedule
        api_response = api_instance.backup_delete_schedule(delete_schedule_command=delete_schedule_command)
        print("The response of BackupPolicyApi->backup_delete_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_delete_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_schedule_command** | [**DeleteScheduleCommand**](DeleteScheduleCommand.md)|  | [optional] 

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

# **backup_describe_backup**
> str backup_describe_backup(project_id, name)

Get backup info by name

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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    name = 'name_example' # str | 

    try:
        # Get backup info by name
        api_response = api_instance.backup_describe_backup(project_id, name)
        print("The response of BackupPolicyApi->backup_describe_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_describe_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

**str**

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

# **backup_describe_restore**
> str backup_describe_restore(project_id, name)

Get restore info by name

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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    name = 'name_example' # str | 

    try:
        # Get restore info by name
        api_response = api_instance.backup_describe_restore(project_id, name)
        print("The response of BackupPolicyApi->backup_describe_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_describe_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

**str**

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

# **backup_describe_schedule**
> str backup_describe_schedule(project_id, name)

Get schedule info by name

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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    name = 'name_example' # str | 

    try:
        # Get schedule info by name
        api_response = api_instance.backup_describe_schedule(project_id, name)
        print("The response of BackupPolicyApi->backup_describe_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_describe_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

**str**

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

# **backup_import_backup_storage**
> object backup_import_backup_storage(import_backup_storage_location_command)

Import backup storage from source project to target project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.import_backup_storage_location_command import ImportBackupStorageLocationCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    import_backup_storage_location_command = taikunpycore.ImportBackupStorageLocationCommand() # ImportBackupStorageLocationCommand | 

    try:
        # Import backup storage from source project to target project
        api_response = api_instance.backup_import_backup_storage(import_backup_storage_location_command)
        print("The response of BackupPolicyApi->backup_import_backup_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_import_backup_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_backup_storage_location_command** | [**ImportBackupStorageLocationCommand**](ImportBackupStorageLocationCommand.md)|  | 

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

# **backup_list_all_backup_storages**
> ListAllBackupStorageLocations backup_list_all_backup_storages(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List all backup locations

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>Search</b> - Options: <i>metadataName</i>, <i>namespace</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_all_backup_storage_locations import ListAllBackupStorageLocations
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List all backup locations
        api_response = api_instance.backup_list_all_backup_storages(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of BackupPolicyApi->backup_list_all_backup_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_list_all_backup_storages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListAllBackupStorageLocations**](ListAllBackupStorageLocations.md)

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

# **backup_list_all_backups**
> ListAllBackups backup_list_all_backups(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List all backups

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>Search</b> - Options: <i>metadataName</i>, <i>namespace</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_all_backups import ListAllBackups
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List all backups
        api_response = api_instance.backup_list_all_backups(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of BackupPolicyApi->backup_list_all_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_list_all_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListAllBackups**](ListAllBackups.md)

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

# **backup_list_all_delete_backup_requests**
> ListAllDeleteBackupRequests backup_list_all_delete_backup_requests(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List all delete backup requests

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>Search</b> - Options: <i>metadataName</i>, <i>namespace</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_all_delete_backup_requests import ListAllDeleteBackupRequests
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List all delete backup requests
        api_response = api_instance.backup_list_all_delete_backup_requests(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of BackupPolicyApi->backup_list_all_delete_backup_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_list_all_delete_backup_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListAllDeleteBackupRequests**](ListAllDeleteBackupRequests.md)

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

# **backup_list_all_restores**
> ListAllRestores backup_list_all_restores(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List all restores

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>Search</b> - Options: <i>metadataName</i>, <i>namespace</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_all_restores import ListAllRestores
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List all restores
        api_response = api_instance.backup_list_all_restores(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of BackupPolicyApi->backup_list_all_restores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_list_all_restores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListAllRestores**](ListAllRestores.md)

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

# **backup_list_all_schedules**
> ListAllSchedules backup_list_all_schedules(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)

List all schedules

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>Search</b> - Options: <i>metadataName</i>, <i>namespace</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.list_all_schedules import ListAllSchedules
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    project_id = 56 # int | 
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List all schedules
        api_response = api_instance.backup_list_all_schedules(project_id, sort_by=sort_by, sort_direction=sort_direction, search=search, limit=limit, offset=offset)
        print("The response of BackupPolicyApi->backup_list_all_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_list_all_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListAllSchedules**](ListAllSchedules.md)

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

# **backup_restore_backup**
> object backup_restore_backup(restore_backup_command=restore_backup_command)

Restore backup

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.restore_backup_command import RestoreBackupCommand
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
    api_instance = taikunpycore.BackupPolicyApi(api_client)
    restore_backup_command = {"projectId":1,"backupName":"test-20240109144001","restoreName":"taikun","includeNamespaces":["taikun.cloud/backup"],"excludeNamespaces":["taikun.cloud/backup"]} # RestoreBackupCommand |  (optional)

    try:
        # Restore backup
        api_response = api_instance.backup_restore_backup(restore_backup_command=restore_backup_command)
        print("The response of BackupPolicyApi->backup_restore_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupPolicyApi->backup_restore_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_backup_command** | [**RestoreBackupCommand**](RestoreBackupCommand.md)|  | [optional] 

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

