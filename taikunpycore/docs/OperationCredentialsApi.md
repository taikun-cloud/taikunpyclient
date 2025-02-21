# taikunpycore.OperationCredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**opscredentials_create**](OperationCredentialsApi.md#opscredentials_create) | **POST** /api/v1/opscredentials | Add Operation credentials
[**opscredentials_delete**](OperationCredentialsApi.md#opscredentials_delete) | **DELETE** /api/v1/opscredentials/{id} | Remove Operation credential by Id
[**opscredentials_list**](OperationCredentialsApi.md#opscredentials_list) | **GET** /api/v1/opscredentials/list | Retrieve all operation credentials
[**opscredentials_list_by_organization_id**](OperationCredentialsApi.md#opscredentials_list_by_organization_id) | **GET** /api/v1/opscredentials | Retrieve operation credentials by organization Id
[**opscredentials_lock_manager**](OperationCredentialsApi.md#opscredentials_lock_manager) | **POST** /api/v1/opscredentials/lockmanager | Lock/Unlock operation credential
[**opscredentials_make_default**](OperationCredentialsApi.md#opscredentials_make_default) | **POST** /api/v1/opscredentials/makedefault | Choose default operation credential
[**opscredentials_metric_names**](OperationCredentialsApi.md#opscredentials_metric_names) | **GET** /api/v1/opscredentials/{id}/metric/names | Fetch prometheus metric names


# **opscredentials_create**
> ApiResponse opscredentials_create(operation_credentials_create_command)

Add Operation credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.operation_credentials_create_command import OperationCredentialsCreateCommand
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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    operation_credentials_create_command = taikunpycore.OperationCredentialsCreateCommand() # OperationCredentialsCreateCommand | 

    try:
        # Add Operation credentials
        api_response = api_instance.opscredentials_create(operation_credentials_create_command)
        print("The response of OperationCredentialsApi->opscredentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_credentials_create_command** | [**OperationCredentialsCreateCommand**](OperationCredentialsCreateCommand.md)|  | 

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

# **opscredentials_delete**
> opscredentials_delete(id)

Remove Operation credential by Id

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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    id = 56 # int | 

    try:
        # Remove Operation credential by Id
        api_instance.opscredentials_delete(id)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_delete: %s\n" % e)
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

# **opscredentials_list**
> OperationCredentials opscredentials_list(limit=limit, offset=offset, organization_id=organization_id, search=search, search_id=search_id, id=id, sort_by=sort_by, sort_direction=sort_direction)

Retrieve all operation credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.operation_credentials import OperationCredentials
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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # Retrieve all operation credentials
        api_response = api_instance.opscredentials_list(limit=limit, offset=offset, organization_id=organization_id, search=search, search_id=search_id, id=id, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of OperationCredentialsApi->opscredentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

### Return type

[**OperationCredentials**](OperationCredentials.md)

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

# **opscredentials_list_by_organization_id**
> List[OperationCredentialsForOrganizationEntity] opscredentials_list_by_organization_id(organization_id=organization_id, search=search)

Retrieve operation credentials by organization Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.operation_credentials_for_organization_entity import OperationCredentialsForOrganizationEntity
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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve operation credentials by organization Id
        api_response = api_instance.opscredentials_list_by_organization_id(organization_id=organization_id, search=search)
        print("The response of OperationCredentialsApi->opscredentials_list_by_organization_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_list_by_organization_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[OperationCredentialsForOrganizationEntity]**](OperationCredentialsForOrganizationEntity.md)

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

# **opscredentials_lock_manager**
> object opscredentials_lock_manager(operation_credential_lock_manager_command)

Lock/Unlock operation credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.operation_credential_lock_manager_command import OperationCredentialLockManagerCommand
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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    operation_credential_lock_manager_command = taikunpycore.OperationCredentialLockManagerCommand() # OperationCredentialLockManagerCommand | 

    try:
        # Lock/Unlock operation credential
        api_response = api_instance.opscredentials_lock_manager(operation_credential_lock_manager_command)
        print("The response of OperationCredentialsApi->opscredentials_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_credential_lock_manager_command** | [**OperationCredentialLockManagerCommand**](OperationCredentialLockManagerCommand.md)|  | 

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

# **opscredentials_make_default**
> object opscredentials_make_default(operation_credentials_make_default_command)

Choose default operation credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.operation_credentials_make_default_command import OperationCredentialsMakeDefaultCommand
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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    operation_credentials_make_default_command = taikunpycore.OperationCredentialsMakeDefaultCommand() # OperationCredentialsMakeDefaultCommand | 

    try:
        # Choose default operation credential
        api_response = api_instance.opscredentials_make_default(operation_credentials_make_default_command)
        print("The response of OperationCredentialsApi->opscredentials_make_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_make_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_credentials_make_default_command** | [**OperationCredentialsMakeDefaultCommand**](OperationCredentialsMakeDefaultCommand.md)|  | 

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

# **opscredentials_metric_names**
> List[str] opscredentials_metric_names(id)

Fetch prometheus metric names

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
    api_instance = taikunpycore.OperationCredentialsApi(api_client)
    id = 56 # int | 

    try:
        # Fetch prometheus metric names
        api_response = api_instance.opscredentials_metric_names(id)
        print("The response of OperationCredentialsApi->opscredentials_metric_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationCredentialsApi->opscredentials_metric_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

