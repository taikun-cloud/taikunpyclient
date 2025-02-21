# taikunpycore.ZededaCloudCredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zededa_create**](ZededaCloudCredentialApi.md#zededa_create) | **POST** /api/v1/zededa/create | Add Zededa credentials
[**zededa_edge_nodes**](ZededaCloudCredentialApi.md#zededa_edge_nodes) | **POST** /api/v1/zededa/edge-nodes | Fetch edge nodes for zededa cloud credential
[**zededa_interfaces**](ZededaCloudCredentialApi.md#zededa_interfaces) | **POST** /api/v1/zededa/interfaces | Fetch interfaces for zededa cloud credential
[**zededa_list**](ZededaCloudCredentialApi.md#zededa_list) | **GET** /api/v1/zededa/list | Retrieve list of Zededa cloud credentials
[**zededa_projects**](ZededaCloudCredentialApi.md#zededa_projects) | **POST** /api/v1/zededa/projects | Fetch projects for zededa cloud credential
[**zededa_update_edge_nodes**](ZededaCloudCredentialApi.md#zededa_update_edge_nodes) | **POST** /api/v1/zededa/update/edge-nodes | Update zededa credentials


# **zededa_create**
> ApiResponse zededa_create(create_zededa_command=create_zededa_command)

Add Zededa credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.api_response import ApiResponse
from taikunpycore.models.create_zededa_command import CreateZededaCommand
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
    api_instance = taikunpycore.ZededaCloudCredentialApi(api_client)
    create_zededa_command = taikunpycore.CreateZededaCommand() # CreateZededaCommand |  (optional)

    try:
        # Add Zededa credentials
        api_response = api_instance.zededa_create(create_zededa_command=create_zededa_command)
        print("The response of ZededaCloudCredentialApi->zededa_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZededaCloudCredentialApi->zededa_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_zededa_command** | [**CreateZededaCommand**](CreateZededaCommand.md)|  | [optional] 

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

# **zededa_edge_nodes**
> List[CommonStringBasedDropdownDto] zededa_edge_nodes(zededa_edge_nodes_command=zededa_edge_nodes_command)

Fetch edge nodes for zededa cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto
from taikunpycore.models.zededa_edge_nodes_command import ZededaEdgeNodesCommand
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
    api_instance = taikunpycore.ZededaCloudCredentialApi(api_client)
    zededa_edge_nodes_command = taikunpycore.ZededaEdgeNodesCommand() # ZededaEdgeNodesCommand |  (optional)

    try:
        # Fetch edge nodes for zededa cloud credential
        api_response = api_instance.zededa_edge_nodes(zededa_edge_nodes_command=zededa_edge_nodes_command)
        print("The response of ZededaCloudCredentialApi->zededa_edge_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZededaCloudCredentialApi->zededa_edge_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zededa_edge_nodes_command** | [**ZededaEdgeNodesCommand**](ZededaEdgeNodesCommand.md)|  | [optional] 

### Return type

[**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md)

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

# **zededa_interfaces**
> List[str] zededa_interfaces(zededa_interface_command=zededa_interface_command)

Fetch interfaces for zededa cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.zededa_interface_command import ZededaInterfaceCommand
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
    api_instance = taikunpycore.ZededaCloudCredentialApi(api_client)
    zededa_interface_command = taikunpycore.ZededaInterfaceCommand() # ZededaInterfaceCommand |  (optional)

    try:
        # Fetch interfaces for zededa cloud credential
        api_response = api_instance.zededa_interfaces(zededa_interface_command=zededa_interface_command)
        print("The response of ZededaCloudCredentialApi->zededa_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZededaCloudCredentialApi->zededa_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zededa_interface_command** | [**ZededaInterfaceCommand**](ZededaInterfaceCommand.md)|  | [optional] 

### Return type

**List[str]**

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

# **zededa_list**
> ZededaList zededa_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)

Retrieve list of Zededa cloud credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.zededa_list import ZededaList
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
    api_instance = taikunpycore.ZededaCloudCredentialApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    organization_id = 56 # int |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    search_id = 'search_id_example' # str |  (optional)
    id = 56 # int |  (optional)

    try:
        # Retrieve list of Zededa cloud credentials
        api_response = api_instance.zededa_list(limit=limit, offset=offset, organization_id=organization_id, sort_by=sort_by, sort_direction=sort_direction, search=search, search_id=search_id, id=id)
        print("The response of ZededaCloudCredentialApi->zededa_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZededaCloudCredentialApi->zededa_list: %s\n" % e)
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

[**ZededaList**](ZededaList.md)

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

# **zededa_projects**
> List[CommonStringBasedDropdownDto] zededa_projects(zededa_projects_command=zededa_projects_command)

Fetch projects for zededa cloud credential

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto
from taikunpycore.models.zededa_projects_command import ZededaProjectsCommand
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
    api_instance = taikunpycore.ZededaCloudCredentialApi(api_client)
    zededa_projects_command = taikunpycore.ZededaProjectsCommand() # ZededaProjectsCommand |  (optional)

    try:
        # Fetch projects for zededa cloud credential
        api_response = api_instance.zededa_projects(zededa_projects_command=zededa_projects_command)
        print("The response of ZededaCloudCredentialApi->zededa_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZededaCloudCredentialApi->zededa_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zededa_projects_command** | [**ZededaProjectsCommand**](ZededaProjectsCommand.md)|  | [optional] 

### Return type

[**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md)

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

# **zededa_update_edge_nodes**
> object zededa_update_edge_nodes(update_edge_nodes_command=update_edge_nodes_command)

Update zededa credentials

### Example

* Api Key Authentication (Bearer):

```python
import taikunpycore
from taikunpycore.models.update_edge_nodes_command import UpdateEdgeNodesCommand
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
    api_instance = taikunpycore.ZededaCloudCredentialApi(api_client)
    update_edge_nodes_command = taikunpycore.UpdateEdgeNodesCommand() # UpdateEdgeNodesCommand |  (optional)

    try:
        # Update zededa credentials
        api_response = api_instance.zededa_update_edge_nodes(update_edge_nodes_command=update_edge_nodes_command)
        print("The response of ZededaCloudCredentialApi->zededa_update_edge_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZededaCloudCredentialApi->zededa_update_edge_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_edge_nodes_command** | [**UpdateEdgeNodesCommand**](UpdateEdgeNodesCommand.md)|  | [optional] 

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

