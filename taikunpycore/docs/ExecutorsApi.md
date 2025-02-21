# taikunpycore.ExecutorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executors_create**](ExecutorsApi.md#executors_create) | **POST** /api/v1/executors/create | Create an executor
[**executors_delete**](ExecutorsApi.md#executors_delete) | **POST** /api/v1/executors/delete | Delete an executor
[**executors_edit_health**](ExecutorsApi.md#executors_edit_health) | **PUT** /api/v1/executors/edit/health | Update health status of the executor by Id
[**executors_list**](ExecutorsApi.md#executors_list) | **GET** /api/v1/executors | Retrieve a list of kube configs of executors
[**executors_toggle**](ExecutorsApi.md#executors_toggle) | **POST** /api/v1/executors/toggle | Toggle an executor


# **executors_create**
> object executors_create(create_executor_command=create_executor_command)

Create an executor

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_executor_command import CreateExecutorCommand
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
    api_instance = taikunpycore.ExecutorsApi(api_client)
    create_executor_command = taikunpycore.CreateExecutorCommand() # CreateExecutorCommand |  (optional)

    try:
        # Create an executor
        api_response = api_instance.executors_create(create_executor_command=create_executor_command)
        print("The response of ExecutorsApi->executors_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutorsApi->executors_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_executor_command** | [**CreateExecutorCommand**](CreateExecutorCommand.md)|  | [optional] 

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

# **executors_delete**
> object executors_delete(delete_executor_command)

Delete an executor

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_executor_command import DeleteExecutorCommand
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
    api_instance = taikunpycore.ExecutorsApi(api_client)
    delete_executor_command = taikunpycore.DeleteExecutorCommand() # DeleteExecutorCommand | 

    try:
        # Delete an executor
        api_response = api_instance.executors_delete(delete_executor_command)
        print("The response of ExecutorsApi->executors_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutorsApi->executors_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_executor_command** | [**DeleteExecutorCommand**](DeleteExecutorCommand.md)|  | 

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

# **executors_edit_health**
> object executors_edit_health(update_executor_health_status_command=update_executor_health_status_command)

Update health status of the executor by Id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_executor_health_status_command import UpdateExecutorHealthStatusCommand
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
    api_instance = taikunpycore.ExecutorsApi(api_client)
    update_executor_health_status_command = taikunpycore.UpdateExecutorHealthStatusCommand() # UpdateExecutorHealthStatusCommand |  (optional)

    try:
        # Update health status of the executor by Id
        api_response = api_instance.executors_edit_health(update_executor_health_status_command=update_executor_health_status_command)
        print("The response of ExecutorsApi->executors_edit_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutorsApi->executors_edit_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_executor_health_status_command** | [**UpdateExecutorHealthStatusCommand**](UpdateExecutorHealthStatusCommand.md)|  | [optional] 

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

# **executors_list**
> ExecutorListResponse executors_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id)

Retrieve a list of kube configs of executors

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.executor_list_response import ExecutorListResponse
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
    api_instance = taikunpycore.ExecutorsApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve a list of kube configs of executors
        api_response = api_instance.executors_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id)
        print("The response of ExecutorsApi->executors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutorsApi->executors_list: %s\n" % e)
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

### Return type

[**ExecutorListResponse**](ExecutorListResponse.md)

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

# **executors_toggle**
> object executors_toggle(toggle_executor_command=toggle_executor_command)

Toggle an executor

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.toggle_executor_command import ToggleExecutorCommand
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
    api_instance = taikunpycore.ExecutorsApi(api_client)
    toggle_executor_command = taikunpycore.ToggleExecutorCommand() # ToggleExecutorCommand |  (optional)

    try:
        # Toggle an executor
        api_response = api_instance.executors_toggle(toggle_executor_command=toggle_executor_command)
        print("The response of ExecutorsApi->executors_toggle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutorsApi->executors_toggle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_executor_command** | [**ToggleExecutorCommand**](ToggleExecutorCommand.md)|  | [optional] 

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

