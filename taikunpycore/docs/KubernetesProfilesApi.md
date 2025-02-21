# taikunpycore.KubernetesProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kubernetesprofiles_create**](KubernetesProfilesApi.md#kubernetesprofiles_create) | **POST** /api/v1/kubernetesprofiles | Add kubernetes profile
[**kubernetesprofiles_delete**](KubernetesProfilesApi.md#kubernetesprofiles_delete) | **DELETE** /api/v1/kubernetesprofiles/{id} | Delete kubernetes profile
[**kubernetesprofiles_dropdown**](KubernetesProfilesApi.md#kubernetesprofiles_dropdown) | **GET** /api/v1/kubernetesprofiles | Retrieve all kubernetes profiles for organization
[**kubernetesprofiles_list**](KubernetesProfilesApi.md#kubernetesprofiles_list) | **GET** /api/v1/kubernetesprofiles/list | Retrieve all kubernetes profiles
[**kubernetesprofiles_lock_manager**](KubernetesProfilesApi.md#kubernetesprofiles_lock_manager) | **POST** /api/v1/kubernetesprofiles/lockmanager | Kubernetes profile lock/unlock


# **kubernetesprofiles_create**
> ApiResponse kubernetesprofiles_create(create_kubernetes_profile_command=create_kubernetes_profile_command)

Add kubernetes profile

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_kubernetes_profile_command import CreateKubernetesProfileCommand
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
    api_instance = taikunpycore.KubernetesProfilesApi(api_client)
    create_kubernetes_profile_command = taikunpycore.CreateKubernetesProfileCommand() # CreateKubernetesProfileCommand |  (optional)

    try:
        # Add kubernetes profile
        api_response = api_instance.kubernetesprofiles_create(create_kubernetes_profile_command=create_kubernetes_profile_command)
        print("The response of KubernetesProfilesApi->kubernetesprofiles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesProfilesApi->kubernetesprofiles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_kubernetes_profile_command** | [**CreateKubernetesProfileCommand**](CreateKubernetesProfileCommand.md)|  | [optional] 

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

# **kubernetesprofiles_delete**
> kubernetesprofiles_delete(id)

Delete kubernetes profile

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
    api_instance = taikunpycore.KubernetesProfilesApi(api_client)
    id = 56 # int | 

    try:
        # Delete kubernetes profile
        api_instance.kubernetesprofiles_delete(id)
    except Exception as e:
        print("Exception when calling KubernetesProfilesApi->kubernetesprofiles_delete: %s\n" % e)
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

# **kubernetesprofiles_dropdown**
> List[KubernetesProfilesEntity] kubernetesprofiles_dropdown(organization_id=organization_id, search=search, cloud_id=cloud_id, offset=offset, limit=limit)

Retrieve all kubernetes profiles for organization

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_profiles_entity import KubernetesProfilesEntity
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
    api_instance = taikunpycore.KubernetesProfilesApi(api_client)
    organization_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    cloud_id = 56 # int |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 1000 # int |  (optional) (default to 1000)

    try:
        # Retrieve all kubernetes profiles for organization
        api_response = api_instance.kubernetesprofiles_dropdown(organization_id=organization_id, search=search, cloud_id=cloud_id, offset=offset, limit=limit)
        print("The response of KubernetesProfilesApi->kubernetesprofiles_dropdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesProfilesApi->kubernetesprofiles_dropdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **cloud_id** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]

### Return type

[**List[KubernetesProfilesEntity]**](KubernetesProfilesEntity.md)

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

# **kubernetesprofiles_list**
> KubernetesProfilesList kubernetesprofiles_list(organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve all kubernetes profiles

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_profiles_list import KubernetesProfilesList
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
    api_instance = taikunpycore.KubernetesProfilesApi(api_client)
    organization_id = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve all kubernetes profiles
        api_response = api_instance.kubernetesprofiles_list(organization_id=organization_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of KubernetesProfilesApi->kubernetesprofiles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesProfilesApi->kubernetesprofiles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**KubernetesProfilesList**](KubernetesProfilesList.md)

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

# **kubernetesprofiles_lock_manager**
> object kubernetesprofiles_lock_manager(kubernetes_profiles_lock_manager_command)

Kubernetes profile lock/unlock

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_profiles_lock_manager_command import KubernetesProfilesLockManagerCommand
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
    api_instance = taikunpycore.KubernetesProfilesApi(api_client)
    kubernetes_profiles_lock_manager_command = taikunpycore.KubernetesProfilesLockManagerCommand() # KubernetesProfilesLockManagerCommand | 

    try:
        # Kubernetes profile lock/unlock
        api_response = api_instance.kubernetesprofiles_lock_manager(kubernetes_profiles_lock_manager_command)
        print("The response of KubernetesProfilesApi->kubernetesprofiles_lock_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesProfilesApi->kubernetesprofiles_lock_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_profiles_lock_manager_command** | [**KubernetesProfilesLockManagerCommand**](KubernetesProfilesLockManagerCommand.md)|  | 

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

