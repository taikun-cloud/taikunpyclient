# taikunpycore.GenericKubernetesCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generic_kubernetes_list**](GenericKubernetesCloudCredentialApi.md#generic_kubernetes_list) | **GET** /api/v1/generic-kubernetes/list | Retrieve list of generic kubernetes cloud credentials
[**generic_kubernetes_update**](GenericKubernetesCloudCredentialApi.md#generic_kubernetes_update) | **PUT** /api/v1/generic-kubernetes/update | Update Generic kubernetes credentials


# **generic_kubernetes_list**
> GenericKubernetesList generic_kubernetes_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of generic kubernetes cloud credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.generic_kubernetes_list import GenericKubernetesList
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
    api_instance = taikunpycore.GenericKubernetesCloudCredentialApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of generic kubernetes cloud credentials
        api_response = api_instance.generic_kubernetes_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of GenericKubernetesCloudCredentialApi->generic_kubernetes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericKubernetesCloudCredentialApi->generic_kubernetes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **organization_id** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **search_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**GenericKubernetesList**](GenericKubernetesList.md)

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

# **generic_kubernetes_update**
> object generic_kubernetes_update(update_generic_kubernetes_command=update_generic_kubernetes_command)

Update Generic kubernetes credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_generic_kubernetes_command import UpdateGenericKubernetesCommand
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
    api_instance = taikunpycore.GenericKubernetesCloudCredentialApi(api_client)
    update_generic_kubernetes_command = taikunpycore.UpdateGenericKubernetesCommand() # UpdateGenericKubernetesCommand |  (optional)

    try:
        # Update Generic kubernetes credentials
        api_response = api_instance.generic_kubernetes_update(update_generic_kubernetes_command=update_generic_kubernetes_command)
        print("The response of GenericKubernetesCloudCredentialApi->generic_kubernetes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericKubernetesCloudCredentialApi->generic_kubernetes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_generic_kubernetes_command** | [**UpdateGenericKubernetesCommand**](UpdateGenericKubernetesCommand.md)|  | [optional] 

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

