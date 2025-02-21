# taikunpycore.S3CredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s3credentials_create**](S3CredentialsApi.md#s3credentials_create) | **POST** /api/v1/s3credentials | Add s3 credential
[**s3credentials_delete**](S3CredentialsApi.md#s3credentials_delete) | **DELETE** /api/v1/s3credentials/{id} | Delete s3 credential
[**s3credentials_dropdown**](S3CredentialsApi.md#s3credentials_dropdown) | **GET** /api/v1/s3credentials | Retrieve all S3 credentials for organization
[**s3credentials_list**](S3CredentialsApi.md#s3credentials_list) | **GET** /api/v1/s3credentials/list | Retrieve all S3 credentials
[**s3credentials_lock_management**](S3CredentialsApi.md#s3credentials_lock_management) | **POST** /api/v1/s3credentials/lockmanager | Lock/unlock s3 credential
[**s3credentials_make_deafult**](S3CredentialsApi.md#s3credentials_make_deafult) | **POST** /api/v1/s3credentials/makedefault | Make default s3 credential
[**s3credentials_update**](S3CredentialsApi.md#s3credentials_update) | **PUT** /api/v1/s3credentials | Update s3 credential


# **s3credentials_create**
> ApiResponse s3credentials_create(backup_credentials_create_command=backup_credentials_create_command)

Add s3 credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.backup_credentials_create_command import BackupCredentialsCreateCommand
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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    backup_credentials_create_command = {"s3Name":"taikun","s3AccessKeyId":"X9BZGP8TSTB7D4K6N9U8","s3SecretKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm","s3Endpoint":"ec2.ap-south-1.amazonaws.com","s3Region":"ap-south-1","organizationId":1} # BackupCredentialsCreateCommand |  (optional)

    try:
        # Add s3 credential
        api_response = api_instance.s3credentials_create(backup_credentials_create_command=backup_credentials_create_command)
        print("The response of S3CredentialsApi->s3credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_credentials_create_command** | [**BackupCredentialsCreateCommand**](BackupCredentialsCreateCommand.md)|  | [optional] 

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

# **s3credentials_delete**
> s3credentials_delete(id)

Delete s3 credential

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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    id = 56 # int | 

    try:
        # Delete s3 credential
        api_instance.s3credentials_delete(id)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **s3credentials_dropdown**
> List[BackupCredentialsForOrganizationEntity] s3credentials_dropdown(organization_id=organization_id, search=search)

Retrieve all S3 credentials for organization

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>Search</b> - Options: <i>name</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_credentials_for_organization_entity import BackupCredentialsForOrganizationEntity
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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve all S3 credentials for organization
        api_response = api_instance.s3credentials_dropdown(organization_id=organization_id, search=search)
        print("The response of S3CredentialsApi->s3credentials_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[BackupCredentialsForOrganizationEntity]**](BackupCredentialsForOrganizationEntity.md)

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

# **s3credentials_list**
> BackupCredentials s3credentials_list(organization_id=organization_id, search=search, search_id=search_id, id=id, sort_by=sort_by, sort_direction=sort_direction, limit=limit, offset=offset)

Retrieve all S3 credentials

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>name</i>, <i>url</i>, <i>region</i>, <i>organizationName</i>, <i>createdAt</i><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i><li><b>Search</b> - Options: <i>name</i>, <i>organizationName</i></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_credentials import BackupCredentials
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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Retrieve all S3 credentials
        api_response = api_instance.s3credentials_list(organization_id=organization_id, search=search, search_id=search_id, id=id, sort_by=sort_by, sort_direction=sort_direction, limit=limit, offset=offset)
        print("The response of S3CredentialsApi->s3credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**BackupCredentials**](BackupCredentials.md)

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

# **s3credentials_lock_management**
> object s3credentials_lock_management(backup_lock_manager_command=backup_lock_manager_command)

Lock/unlock s3 credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_lock_manager_command import BackupLockManagerCommand
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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    backup_lock_manager_command = {"id":1,"mode":"lock|unlock"} # BackupLockManagerCommand |  (optional)

    try:
        # Lock/unlock s3 credential
        api_response = api_instance.s3credentials_lock_management(backup_lock_manager_command=backup_lock_manager_command)
        print("The response of S3CredentialsApi->s3credentials_lock_management:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_lock_management: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_lock_manager_command** | [**BackupLockManagerCommand**](BackupLockManagerCommand.md)|  | [optional] 

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

# **s3credentials_make_deafult**
> object s3credentials_make_deafult(backup_make_default_command=backup_make_default_command)

Make default s3 credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_make_default_command import BackupMakeDefaultCommand
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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    backup_make_default_command = {"id":1} # BackupMakeDefaultCommand |  (optional)

    try:
        # Make default s3 credential
        api_response = api_instance.s3credentials_make_deafult(backup_make_default_command=backup_make_default_command)
        print("The response of S3CredentialsApi->s3credentials_make_deafult:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_make_deafult: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_make_default_command** | [**BackupMakeDefaultCommand**](BackupMakeDefaultCommand.md)|  | [optional] 

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

# **s3credentials_update**
> object s3credentials_update(backup_credentials_update_command=backup_credentials_update_command)

Update s3 credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.backup_credentials_update_command import BackupCredentialsUpdateCommand
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
    api_instance = taikunpycore.S3CredentialsApi(api_client)
    backup_credentials_update_command = {"id":1,"s3Name":"taikun","s3AccessKeyId":"X9BZGP8TSTB7D4K6N9U8","s3SecretKey":"rd98DUXrLkcxI5rqcimJD2BkrsRUZmbqBSwcAcIm"} # BackupCredentialsUpdateCommand |  (optional)

    try:
        # Update s3 credential
        api_response = api_instance.s3credentials_update(backup_credentials_update_command=backup_credentials_update_command)
        print("The response of S3CredentialsApi->s3credentials_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3CredentialsApi->s3credentials_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_credentials_update_command** | [**BackupCredentialsUpdateCommand**](BackupCredentialsUpdateCommand.md)|  | [optional] 

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

