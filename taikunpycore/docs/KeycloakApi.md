# taikunpycore.KeycloakApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keycloak_create**](KeycloakApi.md#keycloak_create) | **POST** /api/v1/keycloak/create | Create keycloak configuration for organization
[**keycloak_delete**](KeycloakApi.md#keycloak_delete) | **POST** /api/v1/keycloak/delete | Delete keycloak configuration
[**keycloak_edit**](KeycloakApi.md#keycloak_edit) | **POST** /api/v1/keycloak/edit | Edit keycloak configuration for organization
[**keycloak_list**](KeycloakApi.md#keycloak_list) | **GET** /api/v1/keycloak | Get keycloak configuration


# **keycloak_create**
> object keycloak_create(keycloak_create_command)

Create keycloak configuration for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.keycloak_create_command import KeycloakCreateCommand
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
    api_instance = taikunpycore.KeycloakApi(api_client)
    keycloak_create_command = taikunpycore.KeycloakCreateCommand() # KeycloakCreateCommand | 

    try:
        # Create keycloak configuration for organization
        api_response = api_instance.keycloak_create(keycloak_create_command)
        print("The response of KeycloakApi->keycloak_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeycloakApi->keycloak_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keycloak_create_command** | [**KeycloakCreateCommand**](KeycloakCreateCommand.md)|  | 

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

# **keycloak_delete**
> object keycloak_delete(keycloak_delete_command)

Delete keycloak configuration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.keycloak_delete_command import KeycloakDeleteCommand
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
    api_instance = taikunpycore.KeycloakApi(api_client)
    keycloak_delete_command = taikunpycore.KeycloakDeleteCommand() # KeycloakDeleteCommand | 

    try:
        # Delete keycloak configuration
        api_response = api_instance.keycloak_delete(keycloak_delete_command)
        print("The response of KeycloakApi->keycloak_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeycloakApi->keycloak_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keycloak_delete_command** | [**KeycloakDeleteCommand**](KeycloakDeleteCommand.md)|  | 

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

# **keycloak_edit**
> object keycloak_edit(keycloak_edit_command)

Edit keycloak configuration for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.keycloak_edit_command import KeycloakEditCommand
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
    api_instance = taikunpycore.KeycloakApi(api_client)
    keycloak_edit_command = taikunpycore.KeycloakEditCommand() # KeycloakEditCommand | 

    try:
        # Edit keycloak configuration for organization
        api_response = api_instance.keycloak_edit(keycloak_edit_command)
        print("The response of KeycloakApi->keycloak_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeycloakApi->keycloak_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keycloak_edit_command** | [**KeycloakEditCommand**](KeycloakEditCommand.md)|  | 

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

# **keycloak_list**
> KeycloakListDto keycloak_list()

Get keycloak configuration

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.keycloak_list_dto import KeycloakListDto
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
    api_instance = taikunpycore.KeycloakApi(api_client)

    try:
        # Get keycloak configuration
        api_response = api_instance.keycloak_list()
        print("The response of KeycloakApi->keycloak_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeycloakApi->keycloak_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**KeycloakListDto**](KeycloakListDto.md)

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

