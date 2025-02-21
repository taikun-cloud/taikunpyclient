# taikunpycore.VirtualClusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_cluster_create**](VirtualClusterApi.md#virtual_cluster_create) | **POST** /api/v1/virtual-cluster/create | Create virtual cluster
[**virtual_cluster_delete**](VirtualClusterApi.md#virtual_cluster_delete) | **POST** /api/v1/virtual-cluster/delete | Delete virtual cluster
[**virtual_cluster_list**](VirtualClusterApi.md#virtual_cluster_list) | **GET** /api/v1/virtual-cluster/{parentProjectId} | Retrieve all vCluster by given project
[**virtual_cluster_quota**](VirtualClusterApi.md#virtual_cluster_quota) | **GET** /api/v1/virtual-cluster/quota/{projectId} | Retrieve vcluster quota details
[**virtual_cluster_visibility**](VirtualClusterApi.md#virtual_cluster_visibility) | **GET** /api/v1/virtual-cluster/visibility/{projectId} | Create button condition visibility


# **virtual_cluster_create**
> virtual_cluster_create(create_virtual_cluster_command=create_virtual_cluster_command)

Create virtual cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.create_virtual_cluster_command import CreateVirtualClusterCommand
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
    api_instance = taikunpycore.VirtualClusterApi(api_client)
    create_virtual_cluster_command = taikunpycore.CreateVirtualClusterCommand() # CreateVirtualClusterCommand |  (optional)

    try:
        # Create virtual cluster
        api_instance.virtual_cluster_create(create_virtual_cluster_command=create_virtual_cluster_command)
    except Exception as e:
        print("Exception when calling VirtualClusterApi->virtual_cluster_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_virtual_cluster_command** | [**CreateVirtualClusterCommand**](CreateVirtualClusterCommand.md)|  | [optional] 

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

# **virtual_cluster_delete**
> object virtual_cluster_delete(delete_virtual_cluster_command)

Delete virtual cluster

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.delete_virtual_cluster_command import DeleteVirtualClusterCommand
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
    api_instance = taikunpycore.VirtualClusterApi(api_client)
    delete_virtual_cluster_command = taikunpycore.DeleteVirtualClusterCommand() # DeleteVirtualClusterCommand | 

    try:
        # Delete virtual cluster
        api_response = api_instance.virtual_cluster_delete(delete_virtual_cluster_command)
        print("The response of VirtualClusterApi->virtual_cluster_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualClusterApi->virtual_cluster_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_virtual_cluster_command** | [**DeleteVirtualClusterCommand**](DeleteVirtualClusterCommand.md)|  | 

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

# **virtual_cluster_list**
> VClusterList virtual_cluster_list(parent_project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve all vCluster by given project

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.v_cluster_list import VClusterList
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
    api_instance = taikunpycore.VirtualClusterApi(api_client)
    parent_project_id = 56 # int | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve all vCluster by given project
        api_response = api_instance.virtual_cluster_list(parent_project_id, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of VirtualClusterApi->virtual_cluster_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualClusterApi->virtual_cluster_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_project_id** | **int**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**VClusterList**](VClusterList.md)

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

# **virtual_cluster_quota**
> KubernetesQuotaListDto virtual_cluster_quota(project_id)

Retrieve vcluster quota details

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.kubernetes_quota_list_dto import KubernetesQuotaListDto
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
    api_instance = taikunpycore.VirtualClusterApi(api_client)
    project_id = 56 # int | 

    try:
        # Retrieve vcluster quota details
        api_response = api_instance.virtual_cluster_quota(project_id)
        print("The response of VirtualClusterApi->virtual_cluster_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualClusterApi->virtual_cluster_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**KubernetesQuotaListDto**](KubernetesQuotaListDto.md)

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

# **virtual_cluster_visibility**
> VClusterActionVisibilityDto virtual_cluster_visibility(project_id)

Create button condition visibility

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.v_cluster_action_visibility_dto import VClusterActionVisibilityDto
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
    api_instance = taikunpycore.VirtualClusterApi(api_client)
    project_id = 56 # int | 

    try:
        # Create button condition visibility
        api_response = api_instance.virtual_cluster_visibility(project_id)
        print("The response of VirtualClusterApi->virtual_cluster_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualClusterApi->virtual_cluster_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**VClusterActionVisibilityDto**](VClusterActionVisibilityDto.md)

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

