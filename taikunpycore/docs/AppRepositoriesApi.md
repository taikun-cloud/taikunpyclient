# taikunpycore.AppRepositoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_available_list**](AppRepositoriesApi.md#repository_available_list) | **GET** /api/v1/repository/available | Retrieve available repositories
[**repository_bind**](AppRepositoriesApi.md#repository_bind) | **POST** /api/v1/repository/bind | Bind repo to organization
[**repository_delete**](AppRepositoriesApi.md#repository_delete) | **POST** /api/v1/repository/delete | Delete repo from organization
[**repository_import**](AppRepositoriesApi.md#repository_import) | **POST** /api/v1/repository/import | Import repo to artifact
[**repository_list**](AppRepositoriesApi.md#repository_list) | **GET** /api/v1/repository/list | Retrieve repo names
[**repository_recommended_list**](AppRepositoriesApi.md#repository_recommended_list) | **GET** /api/v1/repository/recommended | Retrieve taikun recommended repositories
[**repository_unbind**](AppRepositoriesApi.md#repository_unbind) | **POST** /api/v1/repository/unbind | Unbind repo from organization


# **repository_available_list**
> AppRepositoryList repository_available_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, is_private=is_private, organization_id=organization_id)

Retrieve available repositories

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.app_repository_list import AppRepositoryList
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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    is_private = True # bool |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve available repositories
        api_response = api_instance.repository_available_list(offset=offset, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, id=id, is_private=is_private, organization_id=organization_id)
        print("The response of AppRepositoriesApi->repository_available_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_available_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **is_private** | **bool**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**AppRepositoryList**](AppRepositoryList.md)

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

# **repository_bind**
> object repository_bind(bind_app_repository_command=bind_app_repository_command)

Bind repo to organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.bind_app_repository_command import BindAppRepositoryCommand
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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    bind_app_repository_command = taikunpycore.BindAppRepositoryCommand() # BindAppRepositoryCommand |  (optional)

    try:
        # Bind repo to organization
        api_response = api_instance.repository_bind(bind_app_repository_command=bind_app_repository_command)
        print("The response of AppRepositoriesApi->repository_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bind_app_repository_command** | [**BindAppRepositoryCommand**](BindAppRepositoryCommand.md)|  | [optional] 

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

# **repository_delete**
> object repository_delete(delete_repository_command)

Delete repo from organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_repository_command import DeleteRepositoryCommand
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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    delete_repository_command = taikunpycore.DeleteRepositoryCommand() # DeleteRepositoryCommand | 

    try:
        # Delete repo from organization
        api_response = api_instance.repository_delete(delete_repository_command)
        print("The response of AppRepositoriesApi->repository_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_repository_command** | [**DeleteRepositoryCommand**](DeleteRepositoryCommand.md)|  | 

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

# **repository_import**
> object repository_import(import_repo_command=import_repo_command)

Import repo to artifact

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.import_repo_command import ImportRepoCommand
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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    import_repo_command = taikunpycore.ImportRepoCommand() # ImportRepoCommand |  (optional)

    try:
        # Import repo to artifact
        api_response = api_instance.repository_import(import_repo_command=import_repo_command)
        print("The response of AppRepositoriesApi->repository_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_repo_command** | [**ImportRepoCommand**](ImportRepoCommand.md)|  | [optional] 

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

# **repository_list**
> List[str] repository_list(organization_id=organization_id)

Retrieve repo names

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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve repo names
        api_response = api_instance.repository_list(organization_id=organization_id)
        print("The response of AppRepositoriesApi->repository_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

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

# **repository_recommended_list**
> List[ArtifactRepositoryDto] repository_recommended_list(is_taikun=is_taikun, organization_id=organization_id)

Retrieve taikun recommended repositories

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.artifact_repository_dto import ArtifactRepositoryDto
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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    is_taikun = True # bool |  (optional)
    organization_id = 56 # int |  (optional)

    try:
        # Retrieve taikun recommended repositories
        api_response = api_instance.repository_recommended_list(is_taikun=is_taikun, organization_id=organization_id)
        print("The response of AppRepositoriesApi->repository_recommended_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_recommended_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_taikun** | **bool**|  | [optional] 
 **organization_id** | **int**|  | [optional] 

### Return type

[**List[ArtifactRepositoryDto]**](ArtifactRepositoryDto.md)

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

# **repository_unbind**
> object repository_unbind(unbind_app_repository_command)

Unbind repo from organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.unbind_app_repository_command import UnbindAppRepositoryCommand
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
    api_instance = taikunpycore.AppRepositoriesApi(api_client)
    unbind_app_repository_command = taikunpycore.UnbindAppRepositoryCommand() # UnbindAppRepositoryCommand | 

    try:
        # Unbind repo from organization
        api_response = api_instance.repository_unbind(unbind_app_repository_command)
        print("The response of AppRepositoriesApi->repository_unbind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRepositoriesApi->repository_unbind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbind_app_repository_command** | [**UnbindAppRepositoryCommand**](UnbindAppRepositoryCommand.md)|  | 

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

