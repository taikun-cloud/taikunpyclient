# taikunpycore.AllowedHostApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allowedhost_create**](AllowedHostApi.md#allowedhost_create) | **POST** /api/v1/allowedhost/create | Create access profile allowed host
[**allowedhost_delete**](AllowedHostApi.md#allowedhost_delete) | **DELETE** /api/v1/allowedhost/{id} | Delete access profile allowed host
[**allowedhost_edit**](AllowedHostApi.md#allowedhost_edit) | **PUT** /api/v1/allowedhost/edit/{id} | Edit access profile allowed host
[**allowedhost_list**](AllowedHostApi.md#allowedhost_list) | **GET** /api/v1/allowedhost/list/{accessProfileId} | List allowed hosts by access profile id


# **allowedhost_create**
> ApiResponse allowedhost_create(create_allowed_host_command=create_allowed_host_command)

Create access profile allowed host

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_allowed_host_command import CreateAllowedHostCommand
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
    api_instance = taikunpycore.AllowedHostApi(api_client)
    create_allowed_host_command = {"accessProfileId":1,"description":"taikun","ipAddress":"8.8.8.8","maskBits":24} # CreateAllowedHostCommand |  (optional)

    try:
        # Create access profile allowed host
        api_response = api_instance.allowedhost_create(create_allowed_host_command=create_allowed_host_command)
        print("The response of AllowedHostApi->allowedhost_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedHostApi->allowedhost_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_allowed_host_command** | [**CreateAllowedHostCommand**](CreateAllowedHostCommand.md)|  | [optional] 

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

# **allowedhost_delete**
> allowedhost_delete(id)

Delete access profile allowed host

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
    api_instance = taikunpycore.AllowedHostApi(api_client)
    id = 56 # int | 

    try:
        # Delete access profile allowed host
        api_instance.allowedhost_delete(id)
    except Exception as e:
        print("Exception when calling AllowedHostApi->allowedhost_delete: %s\n" % e)
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

# **allowedhost_edit**
> allowedhost_edit(id, edit_allowed_host_dto=edit_allowed_host_dto)

Edit access profile allowed host

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.edit_allowed_host_dto import EditAllowedHostDto
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
    api_instance = taikunpycore.AllowedHostApi(api_client)
    id = 56 # int | 
    edit_allowed_host_dto = {"description":"taikun","ipAddress":"8.8.8.8","maskBits":24} # EditAllowedHostDto |  (optional)

    try:
        # Edit access profile allowed host
        api_instance.allowedhost_edit(id, edit_allowed_host_dto=edit_allowed_host_dto)
    except Exception as e:
        print("Exception when calling AllowedHostApi->allowedhost_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **edit_allowed_host_dto** | [**EditAllowedHostDto**](EditAllowedHostDto.md)|  | [optional] 

### Return type

void (empty response body)

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

# **allowedhost_list**
> AllowedHostList allowedhost_list(access_profile_id, offset=offset, limit=limit, search=search, sort_by=sort_by, sort_direction=sort_direction)

List allowed hosts by access profile id

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.allowed_host_list import AllowedHostList
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
    api_instance = taikunpycore.AllowedHostApi(api_client)
    access_profile_id = 56 # int | 
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # List allowed hosts by access profile id
        api_response = api_instance.allowedhost_list(access_profile_id, offset=offset, limit=limit, search=search, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of AllowedHostApi->allowedhost_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedHostApi->allowedhost_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_profile_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

### Return type

[**AllowedHostList**](AllowedHostList.md)

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

