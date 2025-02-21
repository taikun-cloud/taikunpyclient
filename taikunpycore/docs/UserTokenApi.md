# taikunpycore.UserTokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usertoken_available_endpoints**](UserTokenApi.md#usertoken_available_endpoints) | **GET** /api/v1/usertoken/available-endpoints | Get available endpoint list
[**usertoken_bind_unbind**](UserTokenApi.md#usertoken_bind_unbind) | **POST** /api/v1/usertoken/bind-unbind | Bind and unbind endpoints
[**usertoken_create**](UserTokenApi.md#usertoken_create) | **POST** /api/v1/usertoken/create | Create a new user token
[**usertoken_delete**](UserTokenApi.md#usertoken_delete) | **DELETE** /api/v1/usertoken/delete/{id} | Delete user token
[**usertoken_list**](UserTokenApi.md#usertoken_list) | **GET** /api/v1/usertoken/list | Get user token list


# **usertoken_available_endpoints**
> AvailableEndpointsList usertoken_available_endpoints(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, is_add=is_add, is_readonly=is_readonly)

Get available endpoint list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.available_endpoints_list import AvailableEndpointsList
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
    api_instance = taikunpycore.UserTokenApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    is_add = True # bool |  (optional)
    is_readonly = True # bool |  (optional)

    try:
        # Get available endpoint list
        api_response = api_instance.usertoken_available_endpoints(limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, is_add=is_add, is_readonly=is_readonly)
        print("The response of UserTokenApi->usertoken_available_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTokenApi->usertoken_available_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **is_add** | **bool**|  | [optional] 
 **is_readonly** | **bool**|  | [optional] 

### Return type

[**AvailableEndpointsList**](AvailableEndpointsList.md)

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

# **usertoken_bind_unbind**
> object usertoken_bind_unbind(bind_unbind_endpoint_to_token_command=bind_unbind_endpoint_to_token_command)

Bind and unbind endpoints

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_unbind_endpoint_to_token_command import BindUnbindEndpointToTokenCommand
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
    api_instance = taikunpycore.UserTokenApi(api_client)
    bind_unbind_endpoint_to_token_command = taikunpycore.BindUnbindEndpointToTokenCommand() # BindUnbindEndpointToTokenCommand |  (optional)

    try:
        # Bind and unbind endpoints
        api_response = api_instance.usertoken_bind_unbind(bind_unbind_endpoint_to_token_command=bind_unbind_endpoint_to_token_command)
        print("The response of UserTokenApi->usertoken_bind_unbind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTokenApi->usertoken_bind_unbind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_unbind_endpoint_to_token_command** | [**BindUnbindEndpointToTokenCommand**](BindUnbindEndpointToTokenCommand.md)|  | [optional] 

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

# **usertoken_create**
> UserTokenCreateDto usertoken_create(user_token_create_command)

Create a new user token

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.user_token_create_command import UserTokenCreateCommand
from taikunpycore.models.user_token_create_dto import UserTokenCreateDto
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
    api_instance = taikunpycore.UserTokenApi(api_client)
    user_token_create_command = taikunpycore.UserTokenCreateCommand() # UserTokenCreateCommand | 

    try:
        # Create a new user token
        api_response = api_instance.usertoken_create(user_token_create_command)
        print("The response of UserTokenApi->usertoken_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTokenApi->usertoken_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token_create_command** | [**UserTokenCreateCommand**](UserTokenCreateCommand.md)|  | 

### Return type

[**UserTokenCreateDto**](UserTokenCreateDto.md)

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

# **usertoken_delete**
> usertoken_delete(id)

Delete user token

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
    api_instance = taikunpycore.UserTokenApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete user token
        api_instance.usertoken_delete(id)
    except Exception as e:
        print("Exception when calling UserTokenApi->usertoken_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usertoken_list**
> List[UserTokensListDto] usertoken_list()

Get user token list

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.user_tokens_list_dto import UserTokensListDto
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
    api_instance = taikunpycore.UserTokenApi(api_client)

    try:
        # Get user token list
        api_response = api_instance.usertoken_list()
        print("The response of UserTokenApi->usertoken_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTokenApi->usertoken_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserTokensListDto]**](UserTokensListDto.md)

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

