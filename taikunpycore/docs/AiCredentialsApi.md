# taikunpycore.AiCredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_credential_create**](AiCredentialsApi.md#ai_credential_create) | **POST** /api/v1/ai-credential/create | Create ai credential
[**ai_credential_delete**](AiCredentialsApi.md#ai_credential_delete) | **DELETE** /api/v1/ai-credential/{id} | Remove ai credential
[**ai_credential_dropdown**](AiCredentialsApi.md#ai_credential_dropdown) | **GET** /api/v1/ai-credential | Retrieve all AI credentials for organization
[**ai_credential_list**](AiCredentialsApi.md#ai_credential_list) | **GET** /api/v1/ai-credential/list | Retrieve all AI credentials


# **ai_credential_create**
> ApiResponse ai_credential_create(create_ai_credential_command=create_ai_credential_command)

Create ai credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_ai_credential_command import CreateAiCredentialCommand
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
    api_instance = taikunpycore.AiCredentialsApi(api_client)
    create_ai_credential_command = {"name":"taikun","apiKey":"sk-xxxxxxxxx","organizationId":null} # CreateAiCredentialCommand |  (optional)

    try:
        # Create ai credential
        api_response = api_instance.ai_credential_create(create_ai_credential_command=create_ai_credential_command)
        print("The response of AiCredentialsApi->ai_credential_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiCredentialsApi->ai_credential_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ai_credential_command** | [**CreateAiCredentialCommand**](CreateAiCredentialCommand.md)|  | [optional] 

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

# **ai_credential_delete**
> ai_credential_delete(id)

Remove ai credential

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
    api_instance = taikunpycore.AiCredentialsApi(api_client)
    id = 56 # int | 

    try:
        # Remove ai credential
        api_instance.ai_credential_delete(id)
    except Exception as e:
        print("Exception when calling AiCredentialsApi->ai_credential_delete: %s\n" % e)
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

# **ai_credential_dropdown**
> List[AiCredentialsForOrganizationEntity] ai_credential_dropdown(organization_id=organization_id, search=search)

Retrieve all AI credentials for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ai_credentials_for_organization_entity import AiCredentialsForOrganizationEntity
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
    api_instance = taikunpycore.AiCredentialsApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Retrieve all AI credentials for organization
        api_response = api_instance.ai_credential_dropdown(organization_id=organization_id, search=search)
        print("The response of AiCredentialsApi->ai_credential_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiCredentialsApi->ai_credential_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[AiCredentialsForOrganizationEntity]**](AiCredentialsForOrganizationEntity.md)

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

# **ai_credential_list**
> AiCredentials ai_credential_list(organization_id=organization_id, search=search, search_id=search_id, id=id, sort_by=sort_by, sort_direction=sort_direction, limit=limit, offset=offset)

Retrieve all AI credentials

<div style='font-family: Arial, sans-serif;'>                         <h2 style='color: #4A90E2;'>Description</h2>                         <ul><li><b>SortBy</b> - Options: <i>createdAt</i>, <i>name</i>, <i>organizationName</i></li><li><b>SortDirection</b> - Options: <i>asc</i>, <i>desc</i></li><li><b>Search</b> - Options: <i>name</i>, <i>organizationName</i></li></ul></div>

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.ai_credentials import AiCredentials
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
    api_instance = taikunpycore.AiCredentialsApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Retrieve all AI credentials
        api_response = api_instance.ai_credential_list(organization_id=organization_id, search=search, search_id=search_id, id=id, sort_by=sort_by, sort_direction=sort_direction, limit=limit, offset=offset)
        print("The response of AiCredentialsApi->ai_credential_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiCredentialsApi->ai_credential_list: %s\n" % e)
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

[**AiCredentials**](AiCredentials.md)

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

